# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.test import TestCase, tag
from reports.models import Reports


@tag('unit-test')
class ReportsTest(TestCase):
    def setUp(self):
        self.date = datetime.today()
        self.report = Reports.objects.create(date=self.date,
                                             content='test test1',
                                             subject='test',
                                             sender_email='test@test.com',
                                             id=1)

    def test_date(self):
        self.date = datetime(2019, 9, 20, 20, 8, 7, 127325)
        self.report.date = self.date
        self.report.save()
        self.assertEqual(self.date, self.report.date)

    def test_content(self):
        self.assertEqual(self.report.content, 'test test1')

    def test_sender_email(self):
        self.assertEqual(self.report.sender_email, 'test@test.com')

    def test_subject_name(self):
        self.assertEqual(self.report.subject, 'test')


    def test_str(self):
        self.assertEqual(self.report.__str__(), 'test@test.com - test test1')

    def test_str_long(self):
        str_test = ''
        for _ in range(55):
            str_test += 'a'
        self.report.content = str_test
        self.assertEqual(self.report.__str__(), 'test@test.com - ' + str_test[:50] + '...')

    def test_content_max_length(self):
        self.assertEqual(self.report._meta.get_field('content').max_length, 500)

    def test_sender_email_max_length(self):
        self.assertEqual(self.report._meta.get_field('sender_email').max_length, 60)

    def test_subject_max_length(self):
        self.assertEqual(self.report._meta.get_field('subject').max_length, 255)
