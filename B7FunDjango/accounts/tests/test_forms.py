# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from accounts.forms import SignUpForm, LoginForm, EmailForm
from accounts.models import User

@tag('unit-test')
class SignUpFormTest(TestCase):
    def setUp(self):
        self.form_data = {'email': 'test@text.com', 'user_name': 'user name',
                          'first_name': 'first name', 'last_name': 'last name',
                          'about': 'This is test', 'password': 'SignUpFormTest12',
                          'confirm_password': 'SignUpFormTest12'}
        self.form = SignUpForm(data=self.form_data)

    def test_first_name_label(self):
        #Assert
        self.assertEqual(self.form.fields['first_name'].label, 'שם פרטי')

    def test_first_name_required(self):
        #Assert
        self.assertTrue(self.form.fields['first_name'].required)

    def test_last_name_label(self):
        #Assert
        self.assertEqual(self.form.fields['last_name'].label, 'שם משפחה')

    def test_last_name_required(self):
        #Assert
        self.assertTrue(self.form.fields['last_name'].required)

    def test_user_name_label(self):
        #Assert
        self.assertEqual(self.form.fields['user_name'].label, 'שם משתמש')

    def test_user_name_required(self):
        #Assert
        self.assertTrue(self.form.fields['user_name'].required)

    def test_email_label(self):
        #Assert
        self.assertEqual(self.form.fields['email'].label, 'דוא"ל')

    def test_email_required(self):
        #Assert
        self.assertTrue(self.form.fields['email'].required)

    def test_profile_image_label(self):
        #Assert
        self.assertEqual(self.form.fields['profile_image'].label, 'תמונת פרופיל')

    def test_profile_image_required(self):
        #Assert
        self.assertFalse(self.form.fields['profile_image'].required)

    def test_password_label(self):
        #Assert
        self.assertEqual(self.form.fields['password'].label, 'סיסמא')

    def test_confirm_password_label(self):
        #Assert
        self.assertEqual(self.form.fields['confirm_password'].label, 'וודא סיסמא')

    def test_about_label(self):
        #Assert
        self.assertEqual(self.form.fields['about'].label, 'ספר על עצמך')

    def test_about_required(self):
        #Assert
        self.assertTrue(self.form.fields['about'].required)

    def test_clean_confirm_password(self):
        #Arrange
        form_data = {'email': 'test@text.com', 'user_name': 'user name',
                     'first_name': 'first name', 'last_name': 'last name',
                     'about': 'This is test', 'password': 'SignUpFormTest12',
                     'confirm_password': 'SignUpFormTest13'}
        form = SignUpForm(data=form_data)
        #Act
        form.is_valid()
        #Assert
        self.assertEqual(form["confirm_password"].errors, ['Confirm password does not match'])

    def test_clean_email(self):
        #Arrange
        User.objects.create(email='test_clean_email@text.com', user_name='user name',
                            first_name='first name', last_name='last name',
                            about='This is test', profile_image=None,)
        #Act
        self.form.data["email"] = 'test_clean_email@text.com'
        self.form.is_valid()
        #Assert
        self.assertEqual(self.form["email"].errors, ['This email is already registered'])

    def test_clean_user_name(self):
        #Arrange
        User.objects.create(email='test_clean_user_name@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)
        #Act
        self.form.is_valid()
        #Assert
        self.assertEqual(self.form["user_name"].errors, ['This user name is already registered'])

    def test_clean_post_clean(self):
        #Arrange
        self.form.data["password"] = "1234"
        #Act
        self.form.is_valid()
        #Assert
        self.assertTrue(len(self.form["password"].errors) > 0)

    def test_save(self):
        #act
        user = self.form.save()
        #Assert
        self.assertEqual(user.email, 'test@text.com')

@tag('unit-test')
class LoginFormTest(TestCase):
    def setUp(self):
        #Arrange
        form_data = {'email': 'test@text.com', 'password': 'SignUpFormTest13'}
        self.form = LoginForm(data=form_data)

    def test_email_label(self):
        #Assert
        self.assertEqual(self.form.fields['email'].label, 'דוא"ל')

    def test_password_label(self):
        #Assert
        self.assertEqual(self.form.fields['password'].label, 'סיסמא')

    def test_email_required(self):
        #Assert
        self.assertTrue(self.form.fields['email'].required)

    def test_password_required(self):
        #Assert
        self.assertTrue(self.form.fields['password'].required)

    def test_clean_user_does_not_exist(self):
        #Act
        self.form.is_valid()
        #Assert
        self.assertEqual(self.form["email"].errors, ['User does not exist'])

    def test_clean_password_does_not_match(self):
        #Arrange
        user = User.objects.create(email='test@text.com', user_name='user name',
                                   first_name='first name', last_name='last name',
                                   about='This is test', profile_image=None,)
        user.set_password("SignUpFormTest12")
        user.save()
        #Act
        self.form.is_valid()
        #Assert
        self.assertEqual(self.form["password"].errors, ['Password does not match user'])

    def test_clean_valid(self):
        #Arrange
        user = User.objects.create(email='test@text.com', user_name='user name',
                                   first_name='first name', last_name='last name',
                                   about='This is test', profile_image=None,)
        user.set_password("SignUpFormTest13")
        user.save()
        #Act
        self.form.is_valid()
        #Assert
        self.assertTrue(len(self.form.errors) == 0)

@tag('unit-test')
class EmailFormTest(TestCase):
    def setUp(self):
        #Act
        form_data = {'subject': 'test',
                     'content': 'test test test test test'}
        self.form = EmailForm(data=form_data)

    def test_subject_required(self):
        #Assert
        self.assertTrue(self.form.fields['subject'].required)

    def test_content_required(self):
        #Assert
        self.assertTrue(self.form.fields['content'].required)
