# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import io
from django.test import TestCase, tag
from Profile.forms import UpdateProfileImage, UpdateUserDetails

@tag('unit-test')
class UpdateProfileImageFormTestCase(TestCase):
    def setUp(self):
        img_file = io.StringIO(
            'GIF87a\x01\x00\x01\x00\x80\x01\x00' +
            '\x00\x00\x00ccc,\x00''\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')
        self.form_data = {'profile_image': img_file}

    def test_profile_image_required(self):
        form = UpdateProfileImage(data=self.form_data)
        self.assertFalse(form.fields['profile_image'].required)

    def test_form_is_valid_with_image(self):
        form = UpdateProfileImage(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_valid_no_image(self):
        form = UpdateProfileImage({'profile_image': None})
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        form = UpdateProfileImage()
        self.assertFalse(form.is_valid())

@tag('unit-test')
class UpdateUserDetailsFormTestCase(TestCase):
    def setUp(self):
        form_data = {'email': 'test@text.com',
                     'user_name': 'user name',
                     'first_name': 'first name',
                     'last_name': 'last name',
                     'about': 'This is test',
                     }
        self.form = UpdateUserDetails(data=form_data)

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

    def test_about_label(self):
        self.assertEqual(self.form.fields['about'].label, 'ספר על עצמך')

    def test_about_required(self):
        self.assertTrue(self.form.fields['about'].required)

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())
