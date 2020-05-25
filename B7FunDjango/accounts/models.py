# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
# pylint: disable=no-self-use

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import truncatechars



class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, user_name, first_name, last_name, password, about="", profile_image=""):
        if not email:
            raise ValueError("user must have an email")
        if not user_name:
            raise ValueError("user must have an user name")
        if not password:
            raise ValueError("user must have password")

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            about=about,
            profile_image=profile_image,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, first_name=None, last_name=None):
        user = self.create_user(
            email=email,
            user_name=user_name,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    user_name = models.CharField(max_length=30, unique=True, verbose_name="user_name")
    first_name = models.CharField(max_length=30, verbose_name="first name")
    last_name = models.CharField(max_length=30, verbose_name="last name")
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True, blank=True, null=True)
    about = models.TextField(max_length=500)
    profile_image = models.ImageField(default='default_profile.png')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    warnings = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    objects = MyUserManager()

    def __str__(self):
        return self.user_name + ' - ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Emails(models.Model):

    subject = models.CharField(max_length=255)
    content1 = models.CharField(max_length=500, verbose_name='content')
    sent = models.TextField()

    @property
    def content(self):
        return truncatechars(self.content1, 100)

    class Meta:
        db_table = 'Emails'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.subject

class Logins(models.Model):
    id = models.IntegerField(primary_key=True)
    user_email = models.EmailField(verbose_name="user email", max_length=60)
    login_month = models.IntegerField()
    login_year = models.IntegerField()

    class Meta:
        db_table = 'user logins'
        verbose_name_plural = 'User logins'
