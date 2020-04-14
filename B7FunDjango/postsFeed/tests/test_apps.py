from django.test import TestCase
from postsFeed.apps import PostsfeedConfig


class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(PostsfeedConfig.name, "postsFeed")