# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.test import TestCase, tag
from django.core.exceptions import ValidationError
from reviews.models import Review


@tag('unit-test')
class ReviewTest(TestCase):
    def setUp(self):
        self.date = datetime.today()
        self.review = Review.objects.create(date=self.date,
                                            review_content='test test1',
                                            sender_email='test@test.com',
                                            sender_user_name='test123',
                                            rating=3,
                                            id=1)

    def test_date(self):
        self.date = datetime(2013, 11, 20, 20, 8, 7, 127325)
        self.review.date = self.date
        self.review.save()
        self.assertEqual(self.date, self.review.date)

    def test_content(self):
        self.assertEqual(self.review.review_content, 'test test1')

    def test_sender_email(self):
        self.assertEqual(self.review.sender_email, 'test@test.com')

    def test_sender_user_name(self):
        self.assertEqual(self.review.sender_user_name, 'test123')

    def test_rating(self):
        self.assertEqual(self.review.rating, 3)

    def test_str(self):
        self.assertEqual(self.review.__str__(), 'test@test.com - test test1')

    def test_str_long(self):
        str_test = ''
        for _ in range(55):
            str_test += 'a'
        self.review.review_content = str_test
        self.assertEqual(self.review.__str__(), 'test@test.com - ' + str_test[:50] + '...')

    def test_review_content_max_length(self):
        self.assertEqual(self.review._meta.get_field('review_content').max_length, 500)

    def test_sender_email_max_length(self):
        self.assertEqual(self.review._meta.get_field('sender_email').max_length, 60)

    def test_sender_user_name_max_length(self):
        self.assertEqual(self.review._meta.get_field('sender_user_name').max_length, 30)

    def test_rating_min_validator(self):
        rev = Review(date=self.date,
                     review_content='test test1',
                     sender_email='test@test.com',
                     sender_user_name='test123',
                     rating=0,
                     id=0)
        try:
            rev.full_clean()
        except ValidationError as err:
            self.assertEqual(str(err), "{'rating': ['Ensure this value is greater than or equal to 1.']}")


    def test_rating_min_validator1(self):
        rev = Review(date=self.date,
                     review_content='test test1',
                     sender_email='test@test.com',
                     sender_user_name='test123',
                     rating=1,
                     id=0)
        rev.save()
        self.assertEqual(Review.objects.filter(rating=1).count(), 1)

    def test_rating_max_validator(self):
        rev = Review(date=self.date,
                     review_content='test test1',
                     sender_email='test@test.com',
                     sender_user_name='test123',
                     rating=6,
                     id=0)

        try:
            rev.full_clean()
        except ValidationError as err:
            self.assertEqual(str(err), "{'rating': ['Ensure this value is less than or equal to 5.']}")


    def test_rating_min_validator5(self):
        rev = Review(date=self.date,
                     review_content='test test1',
                     sender_email='test@test.com',
                     sender_user_name='test123',
                     rating=5,
                     id=0)
        rev.save()
        self.assertEqual(Review.objects.filter(rating=5).count(), 1)
