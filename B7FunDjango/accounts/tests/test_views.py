# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=attribute-defined-outside-init
# pylint: disable=attribute-defined-outside-init

from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User

class LoginViewTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        #Act
        response = self.client.get('/login/')
        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        #Act
        response = self.client.get(reverse('accounts:login'))
        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Act
        response = self.client.get(reverse('accounts:login'))
        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    @tag('unit-test')
    def test_view_contains_form(self):
        #Act
        response = self.client.get(reverse('accounts:login'))
        #Assert
        self.assertIsNotNone(response.context['form'])

    @tag('unit-test')
    def test_login_user(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)

        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('feed:feed'))

    @tag('unit-test')
    def test_login_user_blocked(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password", blocked=True)

        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)

        #assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    @tag('unit-test')
    def test_login_admin(self):
        #Arrange
        User.objects.create_superuser(email='test_login_admin@text.com',
                                      user_name='test_create_super_user',
                                      first_name='first name', last_name='last name',
                                      password="user password")
        form_data = {'email': 'test_login_admin@text.com', 'password': 'user password'}

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)

        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('admin:index'))

    @tag('unit-test')
    def test_login_admin_when_logged(self):
        #Arrange
        User.objects.create_superuser(email='test_login_admin@text.com',
                                      user_name='test_create_super_user',
                                      first_name='first name', last_name='last name',
                                      password="user password")
        self.client.login(email='test_login_admin@text.com', password="user password")

        #Act
        response = self.client.post(reverse('accounts:login'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/index.html')
        self.assertRedirects(response, reverse('admin:index'))

    @tag('integration-test')
    def test_login_and_logout_user(self):
        #Arrange
        #Arrange
        User.objects.create(email='test_login_and_logout@text.com', user_name='test_login_and_logout user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        login_form_data = {'email': 'test_login_and_logout@text.com', 'password': 'user password'}

        #Act
        response = self.client.post(reverse('accounts:login'), data=login_form_data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/feed.html')
        self.assertRedirects(response, reverse('feed:feed'))
        self.assertTrue(response.context['user'].is_authenticated)

        #Act
        response = self.client.get('/logout/', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_login_and_logout_admin(self):
        #Arrange
        User.objects.create_superuser(email='test_login_and_logout_admin@text.com',
                                      user_name='test_create_super_user',
                                      first_name='first name', last_name='last name',
                                      password="user password")
        login_form_data = {'email': 'test_login_and_logout_admin@text.com', 'password': 'user password'}

        #Act
        response = self.client.post(reverse('accounts:login'), data=login_form_data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/index.html')
        self.assertRedirects(response, reverse('admin:index'))
        self.assertTrue(response.context['user'].is_authenticated)

        #Act
        response = self.client.get('/logout/', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)

class SignUpViewTest(TestCase):
    @tag('unit-test')
    def test_view_url_exists_at_desired_location(self):
        #Act
        response = self.client.get('/signup/')
        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_url_accessible_by_name(self):
        #Act
        response = self.client.get(reverse('accounts:signup'))
        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Act
        response = self.client.get(reverse('accounts:signup'))
        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    @tag('unit-test')
    def test_view_signup(self):
        #Arrange
        form_data = {'email': 'test@text.com',
                     'user_name': 'user name', 'first_name': 'first name', 'last_name': 'last name',
                     'about': 'This is test', 'password': 'SignUpFormTest12',
                     'confirm_password': 'SignUpFormTest12'}
        #Act
        response = self.client.post('/signup/', data=form_data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(User.objects.filter(email='test@text.com')), 1)

    @tag('unit-test')
    def test_view_contains_form(self):
        #Act
        response = self.client.get(reverse('accounts:signup'))
        #Assert
        self.assertIsNotNone(response.context['form'])

    @tag('integration-test')
    def test_user_sign_up_and_login(self):
        #Arrange
        sign_up_form_data = {'email': 'test_user_sign_up_and_login@text.com', 'user_name': 'user name', 'first_name': 'first name',
                             'last_name': 'last name', 'about': 'This is test', 'password': 'SignUpLoginTest12',
                             'confirm_password': 'SignUpLoginTest12'}
        login_form_data = {'email': 'test_user_sign_up_and_login@text.com', 'password': 'SignUpLoginTest12'}

        #Act
        response = self.client.post(reverse('accounts:signup'), data=sign_up_form_data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(User.objects.filter(email='test_user_sign_up_and_login@text.com')) > 0)

        #Act
        response = self.client.post(reverse('accounts:login'), data=login_form_data, follow=True)

        #Assert
        self.assertTemplateUsed(response, 'feed/feed.html')
        self.assertRedirects(response, reverse('feed:feed'))
        self.assertTrue(response.context['user'].is_authenticated)

    @tag('integration-test')
    def test_sign_up_and_login_and_logout(self):
        #Arrange
        sign_up_form_data = {'email': 'test_sign_up_and_login_and_logout@text.com', 'user_name': 'user name', 'first_name': 'first name',
                             'last_name': 'last name', 'about': 'This is test', 'password': 'userPassword12',
                             'confirm_password': 'userPassword12'}
        login_form_data = {'email': 'test_sign_up_and_login_and_logout@text.com', 'password': 'userPassword12'}

        #Act
        response = self.client.post(reverse('accounts:signup'), data=sign_up_form_data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(User.objects.filter(email='test_sign_up_and_login_and_logout@text.com')) > 0)

        #Act
        response = self.client.post(reverse('accounts:login'), data=login_form_data, follow=True)

        #Assert
        self.assertTemplateUsed(response, 'feed/feed.html')
        self.assertRedirects(response, reverse('feed:feed'))
        self.assertTrue(response.context['user'].is_authenticated)

        #Act
        response = self.client.get('/logout/', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)


class LogOutViewTest(TestCase):
    @tag('unit-test')
    def test_logout(self):
        #Arrange
        User.objects.create(email='LoginViewTest@text.com', user_name='LoginViewTest user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        self.client.login(email="'LoginViewTest@text.com", password="user password")

        #Act
        response = self.client.get('/logout/', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)
