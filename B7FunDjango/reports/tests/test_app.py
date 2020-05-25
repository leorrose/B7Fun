# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from reports.apps import ReportsConfig

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ReportsConfig.name, "reports")
