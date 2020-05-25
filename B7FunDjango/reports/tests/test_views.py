# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User
from reports.models import Reports


class ReportsViewTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='testPostsFeedTest@text.com',
                                        user_name='PostsFeedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None)
        self.report = Reports.objects.create(content='test test1',
                                             subject='test',
                                             sender_email='test@test.com',
                                             id=1)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reports:report'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('reports:report'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports/report.html')


    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")

        #Act
        response = self.client.get(reverse('reports:report'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

    @tag('unit-test')
    def test_report_post(self):
        form_data = {'content': 'content', 'subject': 'subject'}

        # Act
        response = self.client.post(reverse('reports:report'), data=form_data, follow=True)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/?next=/reports/')

    @tag('unit-test')
    def test_create_report_correct_form_data(self):
        user = User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                                   first_name='first name', last_name='last name', about='This is test',
                                   profile_image=None)
        user.set_password('user password')
        user.save()
        form_data = {'content': 'content', 'subject': 'subject'}

        # Act
        self.client.login(email='test_login_user@text.com', password="user password")
        self.client.post(reverse('reports:report'), data=form_data, follow=True)

        report = Reports.objects.get(id=2)
        self.assertEqual(report.content, 'content')
        self.assertEqual(report.subject, 'subject')

    @tag('unit-test')
    def test_create_report_correct_user_data(self):
        user = User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                                   first_name='first name', last_name='last name', about='This is test',
                                   profile_image=None)
        user.set_password('user password')
        user.save()
        form_data = {'content': 'content', 'subject': 'subject'}
        # Act
        self.client.login(email='test_login_user@text.com', password="user password")
        self.client.post(reverse('reports:report'), data=form_data, follow=True)

        report = Reports.objects.get(id=2)
        self.assertEqual(report.sender_email, 'test_login_user@text.com')
