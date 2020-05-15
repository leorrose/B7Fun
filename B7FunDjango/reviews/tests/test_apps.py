# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from reviews.apps import ReviewsConfig

@tag('unit-test')
class ProfileAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ReviewsConfig.name, "reviews")
