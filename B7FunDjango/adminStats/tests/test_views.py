# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=attribute-defined-outside-init
# pylint: disable=attribute-defined-outside-init

from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User

class LoginViewTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(email='test_login_admin@text.com',
                                                        user_name='test_create_super_user',
                                                        first_name='first name', last_name='last name',
                                                        password="user password")
        self.regular_user = User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                                                first_name='first name', last_name='last name', about='This is test',
                                                profile_image=None, password="user password")

    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        #Arrange
        self.client.force_login(self.admin_user)

        #Act
        response = self.client.get(reverse('adminStats:show_stats', kwargs={'year':2020}))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_view_with_user_redirects(self):
        #Arrange
        self.client.force_login(self.regular_user)

        #Act
        response = self.client.get(reverse('adminStats:show_stats', kwargs={'year':2020}))

        #Assert
        self.assertEqual(response.status_code, 302)
