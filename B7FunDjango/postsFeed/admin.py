# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from .models import PostFeed

admin.site.register(PostFeed)
