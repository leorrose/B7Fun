# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import django
from pytz import unicode
from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User


@tag('unit-test')
class ChatAdminTestCase(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create_superuser(email='test@test.com', user_name='test_create_super_user',
                                                  first_name='first name', last_name='last name', password="user password")

        self.client.login(email='test@test.com', password="user password")

    def test_block_user(self):
        #Arrange
        change_url = reverse("admin:accounts_user_changelist")
        object_list = User.objects.values_list('pk', flat=True)
        data = {'action': 'block_users', django.contrib.admin.ACTION_CHECKBOX_NAME: [unicode(f) for f in object_list]}

        #Act
        self.client.post(change_url, data, follow=True)

        #Assert
        self.assertTrue(User.objects.filter(email='test@test.com')[0].blocked)

    def test_unblock_user(self):
        #Arrange
        change_url = reverse("admin:accounts_user_changelist")
        object_list = User.objects.values_list('pk', flat=True)
        data = {'action': 'unblock_users', django.contrib.admin.ACTION_CHECKBOX_NAME: [unicode(f) for f in object_list]}

        #Act
        self.client.post(change_url, data, follow=True)

        #Assert
        self.assertFalse(User.objects.filter(email='test@test.com')[0].blocked)
