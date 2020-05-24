# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from chat.apps import ChatConfig

@tag('unit-test')
class ChatAppsTestCase(TestCase):
    def test_apps_name(self):
        self.assertEqual(ChatConfig.name, "chat")
