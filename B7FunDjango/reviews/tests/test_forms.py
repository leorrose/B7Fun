# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from reviews.forms import ReviewForm
from reviews.models import Review
from django.core.exceptions import ValidationError

@tag('unit-test')
class ReviewFormTest(TestCase):
    def setUp(self):
        self.data = {'review_content': 'review_content',
                     'rating': 3}
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

    def test_review_content_text(self):
        self.assertEqual(self.form.data['review_content'], 'review_content')

    def test_rating_text(self):
        self.assertEqual(self.form.data['rating'], 3)

    def test_rating_min_validator(self):
        data = {'review_content': 'review_content',
                'rating': 0}
        form = ReviewForm(data=data)
        try:
            form.full_clean()
        except ValidationError as err:
            self.assertEqual(str(err), "{'rating': ['Ensure this value is greater than or equal to 1.']}")

    def test_rating_max_validator(self):
        data = {'review_content': 'review_content',
                'rating': 6}
        form = ReviewForm(data=data)

        try:
            form.full_clean()
        except ValidationError as err:
            self.assertEqual(str(err), "{'rating': ['Ensure this value is less than or equal to 5.']}")
