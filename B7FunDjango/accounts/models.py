from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        if not email:
            raise ValueError("user must have an email")
        if not username:
            raise ValueError("user must have an user name")
        if not password:
            raise ValueError("user must have password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        print(str(user.set_password(password)))
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, password,first_name=None, last_name=None, ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):                             #אולי צריך להוסיף סיסמא
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30,unique=True, verbose_name="username")
    first_name = models.CharField(max_length=30, verbose_name="first name")
    last_name = models.CharField(max_length=30, verbose_name="last name")
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   #verbose?
    objects = MyUserManager()

    def __str__(self):
        return self.username + ' - ' + self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True