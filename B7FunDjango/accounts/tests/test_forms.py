from django.test import TestCase
from accounts.forms import SignUpForm, LoginForm


class SignUpFormTest(TestCase):
    form_data = {'email': 'test@text.com',
                 'user_name': 'user name',
                 'first_name': 'first name',
                 'last_name': 'last name',
                 'about': 'This is test',
                 'profile_image': None,
                 'password': 'hello123',
                 'confirm_password': 'hello123'}
    form = SignUpForm(data=form_data)

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
    """
    def test_profile_image_label(self):
        self.assertEqual(self.form.fields['profile_image'].label, 'תמונת פרופיל')
    """
    def test_profile_image_required(self):
        self.assertFalse(self.form.fields['profile_image'].required)

    def test_password_label(self):
        self.assertEqual(self.form.fields['password'].label, 'סיסמה')

    def test_confirm_password_label(self):
        self.assertEqual(self.form.fields['confirm_password'].label, 'וודא סיסמה')


class LoginFormTest(TestCase):
    form_data = {'email': 'test@text.com',
                 'password': 'hello123',}
    form = LoginForm(data=form_data)

    def test_email_label(self):
        self.assertEqual(self.form.fields['email'].label, 'דוא"ל')

    def test_password_label(self):
        self.assertEqual(self.form.fields['password'].label, 'סיסמה')

    def test_email_required(self):
        self.assertTrue(self.form.fields['email'].required)



