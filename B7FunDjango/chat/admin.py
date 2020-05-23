# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ

from django.contrib import admin
from .models import ChatMessage, AbusiveChatMessage

@admin.register(ChatMessage)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('date', 'sender_email', 'chat_room_type', 'chat_room_id')
    list_display = ('message', 'date', 'sender_email', 'chat_room_type', 'chat_room_id')
    fieldsets = (
        (None, {
            'fields': ('message', 'date', 'sender_email', 'chat_room_type', 'chat_room_id')
        }),
    )
    search_fields = ['message', 'sender_email', 'chat_room_type', 'chat_room_id']

@admin.register(AbusiveChatMessage)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('sender_email',)
    list_display = ('message', 'sender_email')
    fieldsets = (
        (None, {
            'fields': ('message', 'sender_email')
        }),
    )
    search_fields = ['message', 'sender_email']
