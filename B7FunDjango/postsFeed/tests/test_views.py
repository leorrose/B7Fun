# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from accounts.models import User
from postsFeed.models import PostFeed


class PostsFeedTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='testPostsFeedTest@text.com',
                                        user_name='PostsFeedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        PostFeed.objects.create(title='new post',
                                body='post body post body post body post body post body',
                                date=datetime.now(),
                                image=None)
        self.user.set_password('user password')
        self.user.save()
        self.client.force_login(self.user)

    def test_view_url(self):
        response = self.client.get(reverse('postsFeed:admin_posts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('postsFeed:admin_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postsFeed/admin_posts.html')

    def test_view_has_posts(self):
        response = self.client.get(reverse('postsFeed:admin_posts'))
        self.assertEqual(len(response.context["posts"]), 1)
