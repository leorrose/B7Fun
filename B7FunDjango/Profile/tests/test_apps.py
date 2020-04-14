from django.test import TestCase
from Profile.apps import ProfileConfig


class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ProfileConfig.name, "Profile")