# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from accounts.models import User


class FeedTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='feedTest@text.com',
                                        user_name='feedTest user name',
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

    def test_view_creates_community_centers_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['community_centers_json'])

    def test_view_creates_dog_gardens_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['dog_gardens_json'])

    def test_view_creates_elderly_social_club_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['elderly_social_club_json'])

    def test_view_creates_playgrounds_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['playgrounds_json'])

    def test_view_creates_sport_facilities_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['sport_facilities_json'])

    def test_view_creates_urban_nature_json_content(self):
        response = self.client.get(reverse('feed:feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['urban_nature_json'])
