# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from accounts.views import signup_view, login_view, logout_view

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_login_url_resolved(self):
        #Act
        url = reverse('accounts:login')
        #Assert
        self.assertEqual(resolve(url).func, login_view)

    def test_sign_up_url_resolved(self):
        #Act
        url = reverse('accounts:signup')
        #Assert
        self.assertEqual(resolve(url).func, signup_view)

    def test_logout_url_resolved(self):
        #Act
        url = reverse('accounts:logout')
        #Assert
        self.assertEqual(resolve(url).func, logout_view)
