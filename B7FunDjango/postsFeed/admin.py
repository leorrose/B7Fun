# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from .models import PostFeed

@admin.register(PostFeed)
class PostFeedAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ("date",)
    list_display = ("title", "body", "date")
    search_fields = ['title']
