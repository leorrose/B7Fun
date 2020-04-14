from django.test import TestCase
from django.urls import reverse, resolve
from django.test.client import Client
from accounts.models import User

class myProfileTest(TestCase):
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create(email='testmyProfileTest@text.com',
                            user_name='myProfileTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None)
        self.user.set_password('user password')
        self.user.save()
        self.client.force_login(self.user)

    def test_view_url(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/feed.html')