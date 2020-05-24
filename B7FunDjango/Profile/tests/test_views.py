# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from unittest import mock
from django.test import TestCase, tag
from django.urls import reverse
from django.core.files import File
from accounts.models import User


class MyProfileTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='testmy_profileTest@text.com',
                                        user_name='my_profileTest user name',
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
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

    @tag('unit-test')
    def test_view_creates_update_profile_form(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateProfileImageForm'])

    @tag('unit-test')
    def test_view_creates_change_password_form(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'])

    @tag('unit-test')
    def test_view_creates_update_user_details_form(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'])

    @tag('unit-test')
    def test_view_creates_update_user_details_form_with_initial_email(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['email'], self.user.email)

    @tag('unit-test')
    def test_view_creates_update_user_details_form_with_initial_first_name(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['first_name'], self.user.first_name)

    @tag('unit-test')
    def test_view_creates_update_user_details_form_with_initial_last_name(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.context['UpdateUserDetailsForm'].initial['last_name'], self.user.last_name)

    @tag('unit-test')
    def test_view_creates_update_user_details_form_with_initial_about(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['about'], self.user.about)

    @tag('unit-test')
    def test_view_creates_change_password_form_with_old_password_change(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['old_password'].widget.attrs['class'], "form-control")

    @tag('unit-test')
    def test_view_creates_change_password_form_with_new_password1_change(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['new_password1'].widget.attrs['class'], "form-control")

    @tag('unit-test')
    def test_view_creates_change_password_form_with_new_password2_change(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('Profile:my_profile'))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['new_password2'].widget.attrs['class'], "form-control")

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('Profile:my_profile'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('Profile:my_profile'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

    def tearDown(self):
        User.objects.filter(email=self.user.email).delete()

@tag('unit-test')
class EditProfileImageTest(TestCase):
    def setUp(self):
        #Arrange
        self.image_mock = mock.MagicMock(spec=File, name='FileMock')
        self.image_mock.name = 'test.jpg'
        self.user = User.objects.create(email='testedit_profile_imageTest@text.com',
                                        user_name='edit_profile_imageTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=self.image_mock)
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.get(reverse('Profile:edit_profile_image'))

        #Assert
        self.assertEqual(response.status_code, 302)

    @tag('unit-test')
    def test_view_does_not_change_profile_image(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.post(reverse('Profile:edit_profile_image'), data={}, format='multipart', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].profile_image.name, "default_profile.png")

    @tag('unit-test')
    def test_view_with_invalid_form(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.post(reverse('Profile:edit_profile_image'), data={'profile_image': self.image_mock},
                                    format='multipart', follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('Profile:edit_profile_image'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('Profile:edit_profile_image'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

    def tearDown(self):
        User.objects.filter(email=self.user.email).delete()


class EditUserDetailsTest(TestCase):
    def setUp(self):
        #Arrange
        self.data = {"email": 'testedit_user_detailsTest@text.com',
                     "user_name": 'editedit_user_detailsTest user name',
                     "first_name": 'first name',
                     "last_name": 'last name',
                     "about": 'This is test'}
        self.user = User.objects.create(email='testedit_user_detailsTest@text.com',
                                        user_name='editedit_user_detailsTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test')
        self.user2 = User.objects.create(email='testedit_user_detailsTest2@text.com',
                                         user_name='editedit_user_detailsTest2 user name',
                                         first_name='first name',
                                         last_name='last name',
                                         about='This is test')

        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.get(reverse('Profile:edit_user_details'), follow=True)
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_change_first_name(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["first_name"] = "test"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].first_name, "test")

    @tag('unit-test')
    def test_change_last_name(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["last_name"] = "test"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].last_name, "test")

    @tag('unit-test')
    def test_change_user_name(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["user_name"] = "test"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].user_name, "test")

    @tag('unit-test')
    def test_change_email(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["email"] = "test@test.com"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].email, "test@test.com")

    @tag('unit-test')
    def test_change_about(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["about"] = "test"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].about, "test")

    @tag('unit-test')
    def test_change_user_name_exist(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["user_name"] = "editedit_user_detailsTest2 user name"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0)

    @tag('unit-test')
    def test_change_email_exist(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["email"] = "testedit_user_detailsTest2@text.com"

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0)

    @tag('unit-test')
    def test_form_is_invalid(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.post(reverse('Profile:edit_user_details'), data={}, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('Profile:edit_user_details'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('Profile:edit_user_details'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

@tag('unit-test')
class ChangePasswordTest(TestCase):
    def setUp(self):
        #Arrange
        self.data = {"old_password": 'user password',
                     "new_password1": 'user test password',
                     "new_password2": 'user test password'}
        self.user = User.objects.create(email='testedit_user_detailsTest@text.com',
                                        user_name='editedit_user_detailsTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test')

        self.user.set_password('user password')
        self.user.save()

    def test_view_url(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.get(reverse('Profile:change_password'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["first_name"] = "test"

        #Act
        response = self.client.post(reverse('Profile:change_password'), data=self.data, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].check_password("user test password"), True)

    def test_form_is_invalid(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')
        self.data["first_name"] = "test"

        #Act
        response = self.client.post(reverse('Profile:change_password'), data={}, follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('Profile:change_password'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('Profile:change_password'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

class RotatePicTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testrotate_picTest@text.com',
                                        user_name='editrotate_picTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image="test-rotate.png")
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.get(reverse('Profile:rotate_pic'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_view_accessible_only_with_login(self):
        #Arrange
        User.objects.create(email='test_login_user@text.com', user_name='test_login_user user name',
                            first_name='first name', last_name='last name', about='This is test',
                            profile_image=None, password="user password")
        form_data = {'email': 'test_login_user@text.com', 'password': 'user password'}

        #Act
        response = self.client.get(reverse('Profile:rotate_pic'), follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'accounts/login.html')

        #Act
        response = self.client.post(reverse('accounts:login'), data=form_data, follow=True)
        response = self.client.post(reverse('Profile:rotate_pic'), follow=True)


        #assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Profile/my_profile.html')

class ViewUserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='ViewUserProfileTest_picTest@text.com',
                                        user_name='editrotate_picTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image="test-rotate.png")
        self.user.set_password('user password')
        self.user.save()

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.login(email=self.user.email, password='user password')

        #Act
        response = self.client.get(reverse('Profile:show_user_profile', kwargs={'user_email':'ViewUserProfileTest_picTest@text.com'}),
                                   follow=True)

        #Assert
        self.assertEqual(response.status_code, 200)
