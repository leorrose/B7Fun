# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from reports.views import report

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_review_url_resolved(self):
        #Act
        url = reverse('reports:report')
        #Assert
        self.assertEqual(resolve(url).func, report)
