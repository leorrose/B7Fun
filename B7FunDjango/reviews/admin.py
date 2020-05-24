# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("date", "sender_user_name", "sender_email", "rating", "review_content")
    search_fields = ['user_name', 'rating']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
