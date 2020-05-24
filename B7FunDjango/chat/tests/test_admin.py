# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import django
from pytz import unicode
from django.test import TestCase, tag
from django.urls import reverse
from chat.models import AbusiveChatMessage
from accounts.models import User


@tag('unit-test')
class ChatAdminTestCase(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create_superuser(email='test@test.com', user_name='test_create_super_user',
                                                  first_name='first name', last_name='last name', password="user password")

        self.abusive_message = AbusiveChatMessage.objects.create(abusive_message_id=0, sender_email='test@test.com',
                                                                 message='this is a test message')
        self.client.login(email='test@test.com', password="user password")

    def test_marked_as_abusive_warnings_lower_then_2(self):
        #Arrange
        change_url = reverse("admin:chat_abusivechatmessage_changelist")
        object_list = AbusiveChatMessage.objects.values_list('pk', flat=True)
        data = {'action': 'mark_as_abusive', django.contrib.admin.ACTION_CHECKBOX_NAME: [unicode(f) for f in object_list]}

        #Act
        response = self.client.post(change_url, data, follow=True)

        #Assert
        self.assertEqual(response.context["user"].warnings, 1)

    def test_marked_as_abusive_warnings_2(self):
        #Arrange
        change_url = reverse("admin:chat_abusivechatmessage_changelist")
        object_list = AbusiveChatMessage.objects.values_list('pk', flat=True)
        data = {'action': 'mark_as_abusive', django.contrib.admin.ACTION_CHECKBOX_NAME: [unicode(f) for f in object_list]}
        self.user.warnings = 2
        self.user.save()

        #Act
        self.client.post(change_url, data, follow=True)

        #Assert
        self.assertEqual(User.objects.filter(email='test@test.com')[0].warnings, 3)

    def test_marked_as_nonabusive(self):
        #Arrange
        change_url = reverse("admin:chat_abusivechatmessage_changelist")
        object_list = AbusiveChatMessage.objects.values_list('pk', flat=True)
        data = {'action': 'mark_as_nonabusive', django.contrib.admin.ACTION_CHECKBOX_NAME: [unicode(f) for f in object_list]}

        #Act
        self.client.post(change_url, data, follow=True)

        #Assert
        self.assertEqual(len(AbusiveChatMessage.objects.values_list('pk', flat=True)), 0)
