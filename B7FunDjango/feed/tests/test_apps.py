from django.test import TestCase
from feed.apps import FeedConfig


class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(FeedConfig.name, "feed")