# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=attribute-defined-outside-init

from datetime import datetime
from django.test import TestCase, tag
from chat.models import ChatMessage, AbusiveChatMessage

@tag('unit-test')
class ChatMessageTest(TestCase):
    def setUp(self):
        #Arrange
        self.message = ChatMessage.objects.create(message_id=0, sender_email='test@test.com', message='this is a test message',
                                                  chat_room_type="test_type", chat_room_id=53)

    def test_chat_message_id(self):
        #Assert
        self.assertEqual(self.message.message_id, 0)

    def test_chat_message_message(self):
        #Assert
        self.assertEqual(self.message.message, 'this is a test message')

    def test_chat_message_sender_email(self):
        #Assert
        self.assertEqual(self.message.sender_email, 'test@test.com')

    def test_chat_message_chat_room_type(self):
        #Assert
        self.assertEqual(self.message.chat_room_type, 'test_type')

    def test_chat_message_chat_room_id(self):
        #Assert
        self.assertEqual(self.message.chat_room_id, 53)

    def test_date(self):
        #Arrange
        self.date = datetime(2013, 11, 20, 20, 8, 7, 127325)

        #Act
        self.message.date = self.date
        self.message.save()

        #Assert
        self.assertEqual(self.date, self.message.date)


@tag('unit-test')
class AbusiveChatMessageTest(TestCase):
    def setUp(self):
        #Arrange
        self.abusive_message = AbusiveChatMessage.objects.create(abusive_message_id=0, sender_email='test@test.com',
                                                                 message='this is a test message')

    def test_chat_message_id(self):
        #Assert
        self.assertEqual(self.abusive_message.abusive_message_id, 0)

    def test_chat_message_message(self):
        #Assert
        self.assertEqual(self.abusive_message.message, 'this is a test message')

    def test_chat_message_sender_email(self):
        #Assert
        self.assertEqual(self.abusive_message.sender_email, 'test@test.com')

    def test_date(self):
        #Arrange
        self.date = datetime(2013, 11, 20, 20, 8, 7, 127325)

        #Act
        self.abusive_message.date = self.date
        self.abusive_message.save()

        #Assert
        self.assertEqual(self.date, self.abusive_message.date)
