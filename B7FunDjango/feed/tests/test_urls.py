# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from feed.views import feed

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_login_url_resolved(self):
        #Act
        url = reverse('feed:feed')
        #Assert
        self.assertEqual(resolve(url).func, feed)
