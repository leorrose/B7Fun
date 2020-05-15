# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from Profile.apps import ProfileConfig

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ProfileConfig.name, "Profile")
