# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from accounts.apps import AccountsConfig

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        #Assert
        self.assertEqual(AccountsConfig.name, "accounts")
