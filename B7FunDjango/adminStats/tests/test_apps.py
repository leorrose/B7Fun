# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from adminStats.apps import AdminstatsConfig

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        #Assert
        self.assertEqual(AdminstatsConfig.name, "adminStats")
