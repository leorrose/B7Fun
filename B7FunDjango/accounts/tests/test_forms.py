from django.test import TestCase
from accounts.forms import SignUpForm, LoginForm

class SignUpFormTest(TestCase):
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        form = SignUpForm(email='test@text.com',
                   user_name='user name',
                   first_name='first name',
                   last_name='last name',
                   about='This is test',
                   profile_image=None,
                   password='hello123',
                   confirm_password='hello123')


