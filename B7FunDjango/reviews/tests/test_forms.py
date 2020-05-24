# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from reviews.forms import ReviewForm

@tag('unit-test')
class ReviewFormTest(TestCase):
    def setUp(self):
        self.data = {'review_content': 'review_content', 'rating': 3}
        self.form = ReviewForm(data=self.data)

    def test_review_content_label(self):
        #Assert
        self.assertEqual(self.form.fields['review_content'].label, 'תגובה')

    def test_rating_label(self):
        #Assert
        self.assertEqual(self.form.fields['rating'].label, 'דרג')

    def test_review_content_required(self):
        #Assert
        self.assertTrue(self.form.fields['review_content'].required)

    def test_rating_required(self):
        #Assert
        self.assertTrue(self.form.fields['rating'].required)
