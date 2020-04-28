# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
