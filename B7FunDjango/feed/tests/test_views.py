# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User

class FeedTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='feedTest@text.com',
                                        user_name='feedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed/feed.html')

    @tag('unit-test')
    def test_view_creates_community_centers_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['community_centers_json'])

    @tag('unit-test')
    def test_view_creates_dog_gardens_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['dog_gardens_json'])

    @tag('unit-test')
    def test_view_creates_elderly_social_club_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['elderly_social_club_json'])

    @tag('unit-test')
    def test_view_creates_playgrounds_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['playgrounds_json'])

    @tag('unit-test')
    def test_view_creates_sport_facilities_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['sport_facilities_json'])

    @tag('unit-test')
    def test_view_creates_urban_nature_json_content(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('feed:feed'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['urban_nature_json'])

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('feed:feed'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)

        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('feed:feed'))
