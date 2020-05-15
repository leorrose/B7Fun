# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from postsFeed.views import admin_posts

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_login_url_resolved(self):
        #Act
        url = reverse('postsFeed:admin_posts')
        #Assert
        self.assertEqual(resolve(url).func, admin_posts)
