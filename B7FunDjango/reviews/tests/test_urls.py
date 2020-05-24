# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from reviews.views import review, reviews_list

@tag('unit-test')
class AccountsUrlsTest(TestCase):
    def test_review_url_resolved(self):
        #Act
        url = reverse('reviews:review')
        #Assert
        self.assertEqual(resolve(url).func, review)

    def test_reviews_list_url_resolved(self):
        #Act
        url = reverse('reviews:reviews_list')
        #Assert
        self.assertEqual(resolve(url).func, reviews_list)
