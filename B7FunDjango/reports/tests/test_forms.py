# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from reports.forms import reportsForm

@tag('unit-test')
class reportsFormTest(TestCase):
    def setUp(self):
        self.data = {'subject': 'subject', 'content': 'content'}
        self.form = reportsForm(data=self.data)

    def test__label(self):
        #Assert
        self.assertEqual(self.form.fields['subject'].label, 'נושא')

    def test_content_label(self):
        #Assert
        self.assertEqual(self.form.fields['content'].label, 'דיווח')

    def test_content_required(self):
        #Assert
        self.assertTrue(self.form.fields['content'].required)

    def test_subject_required(self):
        #Assert
        self.assertTrue(self.form.fields['subject'].required)
