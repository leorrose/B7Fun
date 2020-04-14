from django.test import TestCase
from accounts.apps import AccountsConfig


class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(AccountsConfig.name, "accounts")