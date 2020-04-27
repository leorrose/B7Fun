from django.test import RequestFactory, TestCase
from django.urls import reverse, resolve
from django.test.client import Client
from accounts.models import User
from django.core.files import File
from unittest import mock

class myProfileTest(TestCase):
    def setUp(self):
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
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Profile/myProfile.html')

    def test_view_creates_update_profile_form(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateProfileImageForm'])
    
    def test_view_creates_change_password_form(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'])
        
    def test_view_creates_Update_user_details_form (self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'])
    
    def test_view_creates_Update_user_details_form_with_initial_email(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['email'], self.user.email)

    def test_view_creates_Update_user_details_form_with_initial_first_name(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['first_name'], self.user.first_name)

    def test_view_creates_Update_user_details_form_with_initial_last_name(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['last_name'], self.user.last_name)

    def test_view_creates_Update_user_details_form_with_initial_about(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['UpdateUserDetailsForm'].initial['about'], self.user.about)

    def test_view_creates_change_password_form_with_old_password_change(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['old_password'].widget.attrs['class'], "form-control")

    def test_view_creates_change_password_form_with_new_password1_change(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['new_password1'].widget.attrs['class'], "form-control")
    
    def test_view_creates_change_password_form_with_new_password2_change(self):
        response = self.client.get(reverse('Profile:myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['changePasswordForm'].fields['new_password2'].widget.attrs['class'], "form-control")
        
    def tearDown(self):
        User.objects.filter(email=self.user.email).delete()

class editProfileImageTest(TestCase):
    def setUp(self):
        self.image_mock = mock.MagicMock(spec=File, name='FileMock')                                                                                                          
        self.image_mock.name = 'test.jpg'
        self.user = User.objects.create(email='testeditProfileImageTest@text.com',
                            user_name='editProfileImageTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=self.image_mock)
        self.user.set_password('user password')
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='user password')
    
    def test_view_url(self):
        response = self.client.get(reverse('Profile:editProfileImage'))
        self.assertEqual(response.status_code, 302)

    def test_view_does_not_change_profile_image(self):
        response = self.client.post(reverse('Profile:editProfileImage'), data={}, format='multipart', follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].profile_image.name, "default_profile.png")

    def test_view_with_invalid_form(self):
        response = self.client.post(reverse('Profile:editProfileImage'), data={'profile_image': self.image_mock}, format='multipart', follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0 )

    def tearDown(self):
        User.objects.filter(email=self.user.email).delete()

class editUserDetailsTest(TestCase):
    def setUp(self):
        self.data = {"email":'testeditUserDetailsTest@text.com',
        "user_name":'editeditUserDetailsTest user name',
        "first_name":'first name',
        "last_name":'last name',
        "about":'This is test'}
        self.user = User.objects.create(email='testeditUserDetailsTest@text.com',
                            user_name='editeditUserDetailsTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test')
        self.user2 = User.objects.create(email='testeditUserDetailsTest2@text.com',
                            user_name='editeditUserDetailsTest2 user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test')

        self.user.set_password('user password')
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='user password')

    def test_view_url(self):
        response = self.client.get(reverse('Profile:editUserDetails'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_change_first_name(self):
        self.data["first_name"] = "test"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].first_name, "test")

    def test_change_last_name(self):
        self.data["last_name"] = "test"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].last_name, "test")

    def test_change_user_name(self):
        self.data["user_name"] = "test"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].user_name, "test")

    def test_change_email(self):
        self.data["email"] = "test@test.com"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].email, "test@test.com")

    def test_change_about(self):
        self.data["about"] = "test"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].about, "test")

    def test_change_user_name_exist(self):
        self.data["user_name"] = "editeditUserDetailsTest2 user name"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0 )
    
    def test_change_email_exist(self):
        self.data["email"] = "testeditUserDetailsTest2@text.com"
        response = self.client.post(reverse('Profile:editUserDetails'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0 )

    def test_form_is_invalid(self):
        response = self.client.post(reverse('Profile:editUserDetails'), data={}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0 )

class change_passwordTest(TestCase):
    def setUp(self):
        self.data = {"old_password":'user password',
        "new_password1":'user test password',
        "new_password2":'user test password'}
        self.user = User.objects.create(email='testeditUserDetailsTest@text.com',
                            user_name='editeditUserDetailsTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test')

        self.user.set_password('user password')
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='user password')

    def test_view_url(self):
        response = self.client.get(reverse('Profile:change_password'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        self.data["first_name"] = "test"
        response = self.client.post(reverse('Profile:change_password'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].check_password("user test password"), True)

    def test_form_is_invalid(self):
        self.data["first_name"] = "test"
        response = self.client.post(reverse('Profile:change_password'), data={}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["errors"]) > 0 )


class rotatePicTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testrotatePicTest@text.com',
                            user_name='editrotatePicTest user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image="test-rotate.png")
        self.user.set_password('user password')
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='user password')

    def test_view_url(self):
        response = self.client.get(reverse('Profile:rotatePic'), follow=True)
        self.assertEqual(response.status_code, 200)