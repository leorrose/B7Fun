from django.test import TestCase
from django.urls import reverse
from postsFeed.views import posts

class PostsFeedTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 301)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('postsFeed:posts'))
        self.assertEqual(response.status_code, 302)

