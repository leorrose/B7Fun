# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ

from django.contrib import admin
from .models import Reports
# Register your models here.



@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("subject", "sender_email", "date")
    fieldsets = (
        (None, {
            'fields': ('sender_email', 'subject', 'content', 'date')
        }),
    )
    search_fields = ['user_name', 'subject']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
