# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User
from postsFeed.models import PostFeed


class PostsFeedTest(TestCase):
    def setUp(self):
        #Arrange
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

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('postsFeed:admin_posts'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('postsFeed:admin_posts'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postsFeed/admin_posts.html')

    @tag('unit-test')
    def test_view_has_posts(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('postsFeed:admin_posts'))

        #Assert
        self.assertEqual(len(response.context["posts"]), 1)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('postsFeed:admin_posts'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('postsFeed:admin_posts'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'postsFeed/admin_posts.html')
