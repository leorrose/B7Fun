from django.test import TestCase
from accounts.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        User.objects.create(email='test@text.com',
                            user_name='user name',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            profile_image=None,)

    def test_first_name(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.first_name, 'first name')

    def test_first_name_maxlen(self):
        user = User.objects.get(email='test@text.com')
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.last_name, 'last name')

    def test_last_name_maxlen(self):
        user = User.objects.get(email='test@text.com')
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_user_name(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.user_name, 'user name')

    def test_user_name_maxlen(self):
        user = User.objects.get(email='test@text.com')
        max_length = user._meta.get_field('user_name').max_length
        self.assertEquals(max_length, 30)

    def test_about(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.about, 'This is test')

    def test_about_maxlen(self):
        user = User.objects.get(email='test@text.com')
        max_length = user._meta.get_field('about').max_length
        self.assertEquals(max_length, 500)

    def test_is_admin(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.is_admin, False)

    def test_is_active(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.is_active, True)

    def test_is_super_user(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.is_superuser, False)

    def test_is_staff(self):
        user = User.objects.get(email='test@text.com')
        self.assertEqual(user.is_staff, False)

    def test_create_user_no_email(self):
        try:
            User.objects.create_user(email='',
                            user_name='test_create_user_no_email',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            password="test_create_user_no_email",
                            profile_image=None,)
        except ValueError as err:
            self.assertEqual(str(err), "user must have an email")
    
    def test_create_user_no_user_name(self):
        try:
            User.objects.create_user(email='test_create_user_no_user_name@text.com',
                            user_name="",
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            password="test_create_user_no_user_name",
                            profile_image=None,)
        except ValueError as err:
            self.assertEqual(str(err), "user must have an user name")

    def test_create_user_no_password(self):
        try:
            User.objects.create_user(email='test_create_user_no_password@text.com',
                            user_name='test_create_user_no_password',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            password="",
                            profile_image=None,)
        except ValueError as err:
            self.assertEqual(str(err), "user must have password")

    def test_create_super_user(self):
        usr = User.objects.create_superuser(email='test_create_super_user@text.com',
                        user_name='test_create_super_user',
                        first_name='first name',
                        last_name='last name',
                        password="test_create_super_user",)
        self.assertTrue(usr)
        self.assertTrue(usr.has_perm(perm="test"))
    
    def test_user_str(self):
        usr = User.objects.create_user(email='test_create_user_no_password@text.com',
                            user_name='test_create_user_no_password',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            password="test_user_str",
                            profile_image=None,)
        self.assertTrue(usr.__str__(), "test_create_user_no_password-test_create_user_no_password@text.com")

    def test_user_has_module_perms(self):
        usr = User.objects.create_user(email='test_create_user_no_password@text.com',
                            user_name='test_create_user_no_password',
                            first_name='first name',
                            last_name='last name',
                            about='This is test',
                            password="test_user_has_module_perms",
                            profile_image=None,)
        self.assertTrue(usr.has_module_perms(app_label="test"))
    