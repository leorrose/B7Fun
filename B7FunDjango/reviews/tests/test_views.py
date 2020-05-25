# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User
from reviews.models import Review


class ReviewViewTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='testPostsFeedTest@text.com',
                                        user_name='PostsFeedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        self.review = Review.objects.create(review_content='test content',
                                            sender_email='test@email.com',
                                            sender_user_name='test_user_name',
                                            rating=3,
                                            id=1)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reviews:review'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reviews:review'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review.html')


    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")

        #Act
        response = self.client.get(reverse('reviews:review'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

    @tag('unit-test')
    def test_review_post(self):
        form_data = {'review_content': 'content', 'rating': 3}

        # Act
        response = self.client.post(reverse('reviews:review'), data=form_data, follow=True)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/?next=/reviews/')

    @tag('unit-test')
    def test_create_review_correct_form_data(self):
        user = User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                                   first_name='first name', last_name='last name', about='This is test',
                                   profile_image=None)
        user.set_password('user password')
        user.save()
        form_data = {'review_content': 'content', 'rating': 3}

        # Act
        self.client.login(email='test_login_user@text.com', password="user password")
        self.client.post(reverse('reviews:review'), data=form_data, follow=True)

        review = Review.objects.get(id=2)
        self.assertEqual(review.review_content, 'content')
        self.assertEqual(review.rating, 3)

    @tag('unit-test')
    def test_create_review_correct_user_data(self):
        user = User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                                   first_name='first name', last_name='last name', about='This is test',
                                   profile_image=None)
        user.set_password('user password')
        user.save()
        form_data = {'review_content': 'content', 'rating': 3}

        # Act
        self.client.login(email='test_login_user@text.com', password="user password")
        self.client.post(reverse('reviews:review'), data=form_data, follow=True)

        review = Review.objects.get(id=2)
        self.assertEqual(review.sender_email, 'test_login_user@text.com')
        self.assertEqual(review.sender_user_name, 'test_login_user user name')


class ReviewListTest(TestCase):
    def setUp(self):
        # Arrange
        self.user = User.objects.create(email='testPostsFeedTest@text.com',
                                        user_name='PostsFeedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        self.review = Review.objects.create(review_content='test content',
                                            sender_email='test@email.com',
                                            sender_user_name='test_user_name',
                                            rating=3,
                                            id=1)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reviews:reviews_list'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reviews:reviews_list'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews_list.html')

    @tag('unit-test')
    def test_view_has_reviews(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reviews:reviews_list'))

        #Assert
        self.assertEqual(len(response.context["reviews"]), 1)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")

        #Act
        response = self.client.get(reverse('reviews:reviews_list'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')
