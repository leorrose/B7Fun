# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from Profile.views import my_profile, edit_profile_image, edit_user_details, change_password, rotate_pic, show_user_profile

@tag('unit-test')
class UpdateProfileImageFormTestCase(TestCase):
    def test_my_profile_url_is_resolved(self):
        url = reverse('Profile:my_profile')
        self.assertEqual(resolve(url).func, my_profile)

    def test_edit_profile_image_url_is_resolved(self):
        url = reverse('Profile:edit_profile_image')
        self.assertEqual(resolve(url).func, edit_profile_image)

    def test_edit_user_details_url_is_resolved(self):
        url = reverse('Profile:edit_user_details')
        self.assertEqual(resolve(url).func, edit_user_details)

    def test_change_password_url_is_resolved(self):
        url = reverse('Profile:change_password')
        self.assertEqual(resolve(url).func, change_password)

    def test_rotate_pic_url_is_resolved(self):
        url = reverse('Profile:rotate_pic')
        self.assertEqual(resolve(url).func, rotate_pic)

    def test_show_user_profile_is_resolved(self):
        url = reverse('Profile:show_user_profile_no_arg')
        self.assertEqual(resolve(url).func, show_user_profile)

    def test_show_user_profile_with_arg_is_resolved(self):
        url = reverse('Profile:show_user_profile', kwargs={'user_email':'test@gmail.com'})
        self.assertEqual(resolve(url).func, show_user_profile)
