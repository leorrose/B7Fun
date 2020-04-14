from django.test import TestCase
from accounts.forms import SignUpForm, LoginForm
from django import forms
from accounts.models import User

class SignUpFormTest(TestCase):
    def setUpTestData(self):
        self.form_data = {'email': 'test@text.com',
        'user_name': 'user name',
        'first_name': 'first name',
        'last_name': 'last name',
        'about': 'This is test',
        'password': 'SignUpFormTest12',
        'confirm_password': 'SignUpFormTest12'}
        self.form = SignUpForm(data=self.form_data)

    def test_first_name_label(self):
        self.assertEqual(self.form.fields['first_name'].label, 'שם פרטי')

    def test_first_name_required(self):
        self.assertTrue(self.form.fields['first_name'].required)

    def test_last_name_label(self):
        self.assertEqual(self.form.fields['last_name'].label, 'שם משפחה')

    def test_last_name_required(self):
        self.assertTrue(self.form.fields['last_name'].required)

    def test_user_name_label(self):
        self.assertEqual(self.form.fields['user_name'].label, 'שם משתמש')

    def test_user_name_required(self):
        self.assertTrue(self.form.fields['user_name'].required)

    def test_email_label(self):
        self.assertEqual(self.form.fields['email'].label, 'דוא"ל')

    def test_email_required(self):
        self.assertTrue(self.form.fields['email'].required)

    def test_profile_image_label(self):
        self.assertEqual(self.form.fields['profile_image'].label, 'תמונת פרופיל')

    def test_profile_image_required(self):
        self.assertFalse(self.form.fields['profile_image'].required)

    def test_password_label(self):
        self.assertEqual(self.form.fields['password'].label, 'סיסמא')

    def test_confirm_password_label(self):
        self.assertEqual(self.form.fields['confirm_password'].label, 'וודא סיסמא')

    def test_about_label(self):
        self.assertEqual(self.form.fields['about'].label, 'ספר על עצמך')

    def test_about_required(self):
        self.assertTrue(self.form.fields['about'].required)

    def test_clean_confirm_password(self):
        form_data = {'email': 'test@text.com',
        'user_name': 'user name',
        'first_name': 'first name',
        'last_name': 'last name',
        'about': 'This is test',
        'password': 'SignUpFormTest12',
        'confirm_password': 'SignUpFormTest13'}
        form = SignUpForm(data=form_data)
        form.is_valid()
        self.assertEqual(form["confirm_password"].errors, ['Confirm password does not match'])
            
    def test_clean_email(self):
        User.objects.create(email='test_clean_email@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)
        self.form.data["email"] = 'test_clean_email@text.com'
        self.form.is_valid()
        self.assertEqual(self.form["email"].errors, ['This email is already registered'])

    def test_clean_user_name(self):
        User.objects.create(email='test_clean_user_name@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)
        self.form.is_valid()
        self.assertEqual(self.form["user_name"].errors, ['This user name is already registered'])
            
    def test_clean_post_clean(self):
        self.form.data["password"] = "1234"
        self.form.is_valid()
        self.assertTrue(len(self.form["password"].errors) > 0)
    
    def test_save(self):
        user = self.form.save()
        self.assertEqual(user.email, 'test@text.com')

class LoginFormTest(TestCase):
    def setUpTestData(self):
        form_data = {'email': 'test@text.com',
                 'password': 'SignUpFormTest13'}
        self.form = LoginForm(data=form_data)

    def test_email_label(self):
        self.assertEqual(self.form.fields['email'].label, 'דוא"ל')

    def test_password_label(self):
        self.assertEqual(self.form.fields['password'].label, 'סיסמא')

    def test_email_required(self):
        self.assertTrue(self.form.fields['email'].required)
    
    def test_password_required(self):
        self.assertTrue(self.form.fields['password'].required)
    
    def test_clean_user_does_not_exist(self):
        self.form.is_valid()
        self.assertEqual(self.form["email"].errors, ['User does not exist'])
    
    def test_clean_password_does_not_match(self):
        user = User.objects.create(email='test@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)
        user.set_password("SignUpFormTest12")
        user.save()
        self.form.is_valid()
        self.assertEqual(self.form["password"].errors, ['Password does not match user'])
    
    def test_clean_valid(self):
        user = User.objects.create(email='test@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)
        user.set_password("SignUpFormTest13")
        user.save()
        self.form.is_valid()
        self.assertTrue(len(self.form.errors) == 0)



