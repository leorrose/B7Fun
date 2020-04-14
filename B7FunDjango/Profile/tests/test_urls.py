from django.test import TestCase
from django.urls import resolve, reverse
from Profile.views import myProfile, editProfileImage, editUserDetails, change_password, rotatePic

class UpdateProfileImageFormTestCase(TestCase):
    def test_myProfile_url_is_resolved(self):
        url = reverse('Profile:myProfile')
        self.assertEqual(resolve(url).func, myProfile)

    def test_editProfileImage_url_is_resolved(self):
        url = reverse('Profile:editProfileImage')
        self.assertEqual(resolve(url).func, editProfileImage)

    def test_editUserDetails_url_is_resolved(self):
        url = reverse('Profile:editUserDetails')
        self.assertEqual(resolve(url).func, editUserDetails)

    def test_change_password_url_is_resolved(self):    
        url = reverse('Profile:change_password')
        self.assertEqual(resolve(url).func, change_password)

    def test_rotatePic_url_is_resolved(self):
        url = reverse('Profile:rotatePic')
        self.assertEqual(resolve(url).func, rotatePic)

