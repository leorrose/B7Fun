# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase
from feed.apps import FeedConfig


class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(FeedConfig.name, "feed")
