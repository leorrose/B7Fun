# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ("date_joined", 'last_login')
    list_display = ("email", "user_name", "first_name", "last_name")
    fieldsets = (
        (None, {
            'fields': ('email', 'user_name','first_name', 'last_name', 'about', 'profile_image')
        }),
    )
    search_fields = ['first_name', 'last_name']
