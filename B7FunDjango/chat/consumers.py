# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-branches
# pylint: disable=arguments-differ
# pylint: disable=attribute-defined-outside-init
# pylint: disable=unused-argument

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from accounts.models import User
from feed.models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature
from .models import ChatMessage, AbusiveChatMessage

def report_message(obj, text_data_json):
    message = text_data_json["message"]
    sender_email = text_data_json["sender_email"]
    message_id = text_data_json["message_id"]
    messages = AbusiveChatMessage.objects.filter(abusive_message_id=message_id)
    if not messages:
        AbusiveChatMessage.objects.create(abusive_message_id=message_id, message=message, sender_email=sender_email)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_type = self.scope['url_route']['kwargs']['room_type']
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_name = str(self.room_type) + str(self.room_id)
        self.room_group_name = 'chat_%s' % self.room_name

        if self.room_type == "community_centers":
            if len(community_centers.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "dog_gardens":
            if len(dog_gardens.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "elderly_social_club":
            if len(elderly_social_club.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "playgrounds":
            if len(playgrounds.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "sport_facilities":
            if len(sport_facilities.objects.filter(id=self.room_id)) != 1:
                return self.close()
        elif self.room_type == "urban_nature":
            if len(urban_nature.objects.filter(id=self.room_id)) != 1:
                return self.close()
        else:
            return self.close()

        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        return self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.commands[text_data_json['command']](self, text_data_json)


    def fetch_messages(self, text_data_json):
        index = text_data_json['index']
        messages = ChatMessage.objects.filter(chat_room_id=self.room_id,
                                              chat_room_type=self.room_type).order_by('-date')[(index*30):((index+1)*30)]
        messages_list = []

        for i in messages:
            messages_list += [{
                'message': i.message,
                'message_id': i.message_id,
                'sender': i.sender_email,
                'date': i.date.strftime('%d/%m/%Y'),
                'time': i.date.strftime('%H:%M'),
                'profile_image': User.objects.filter(email=i.sender_email)[0].profile_image.name,
                'user_name': User.objects.filter(email=i.sender_email)[0].user_name,
            }]

        self.send(text_data=json.dumps({
            'messages': messages_list,
            'command': 'fetch_messages',
            'scroll_to_end': text_data_json['scroll_to_end']
        }))

    def send_chat_messages(self, text_data_json):
        temp_id = 0
        message = text_data_json["message"]
        max_id = ChatMessage.objects.all().order_by('message_id').last()
        if max_id:
            temp_id = max_id.message_id + 1
        new_message = ChatMessage(message_id=temp_id, message=message, sender_email=self.scope['user'].email, chat_room_id=self.room_id,
                                  chat_room_type=self.room_type)
        new_message.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'message_id': new_message.message_id,
                'sender': self.scope['user'].email,
                'date': new_message.date.strftime('%d/%m/%Y'),
                'time': new_message.date.strftime('%H:%M'),
                'profile_image': self.scope['user'].profile_image.name,
                'user_name': self.scope['user'].user_name,
                'command': 'new_messages'
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        message_id = event['message_id']
        sender = event['sender']
        date = event['date']
        time = event['time']
        profile_image = event['profile_image']
        user_name = event['user_name']
        command = event['command']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'message_id': message_id,
            'sender': sender,
            'date': date,
            'time': time,
            'profile_image': profile_image,
            'user_name': user_name,
            'command': command
        }))

    commands = {'fetch_messages' : fetch_messages, 'new_messages': send_chat_messages, 'report_message': report_message}
