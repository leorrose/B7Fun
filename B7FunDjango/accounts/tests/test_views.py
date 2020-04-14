from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from accounts.models import User
from accounts.views import login_view,signup_view


class LoginViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_redirect_to_feed(self):
        self.client = Client()
        self.user = User.objects.create(email='LoginViewTest@text.com',
                            user_name='LoginViewTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None)
        self.user.set_password('user password')
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.user = User.objects.create(email='LoginViewTest@text.com',
                            user_name='LoginViewTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None)
        self.user.set_password('user password')
        self.user.save()
        form_data = {'email': 'LoginViewTest@text.com',
                 'password': 'user password'}
        response = self.client.post('/login', data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_admin(self):
        self.user = User.objects.create_superuser(email='test_login_admin@text.com',
                        user_name='test_create_super_user',
                        first_name='first name',
                        last_name='last name',
                        password="user password",)
        form_data = {'email': 'test_login_admin@text.com',
                 'password': 'user password'}
        response = self.client.post('/login', data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

class SignUpViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
    
    def test_view_signup(self):
        form_data = {'email': 'test@text.com',
        'user_name': 'user name',
        'first_name': 'first name',
        'last_name': 'last name',
        'about': 'This is test',
        'password': 'SignUpFormTest12',
        'confirm_password': 'SignUpFormTest12'}
        response = self.client.post('/signup',data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

class logOutViewTest(TestCase):
    def test_logout(self):
        self.client = Client()
        self.user = User.objects.create(email='LoginViewTest@text.com',
                            user_name='LoginViewTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None)
        self.user.set_password('user password')
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get('/logout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)