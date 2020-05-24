# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from chat.views import chat_room

@tag('unit-test')
class ChatMessageRoomTestCase(TestCase):
    def test_chat_is_resolved(self):
        url = reverse('chat:chat_room', kwargs={'room_type':'test', 'room_id':4})
        self.assertEqual(resolve(url).func, chat_room)
