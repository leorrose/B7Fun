# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ

from django.contrib import admin
from .models import ChatMessage, AbusiveChatMessage
from accounts.models import User
from .models import ChatMessage
from django.template import loader
from django.core import mail
from django.utils.html import strip_tags

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
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
class AbusiveChatMessageAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('sender_email',)
    list_display = ('message', 'sender_email')
    fieldsets = (
        (None, {
            'fields': ('message', 'sender_email')
        }),
    )
    search_fields = ['message', 'sender_email']

    def mark_as_nonabusive(self, request, queryset):
        self.message_user(request, "Handled {} nonabusive messages".format(queryset.count()))
        queryset.delete()

    def mark_as_abusive(self, request, queryset):
        self.message_user(request, "Handled {} abusive messages".format(queryset.count()))
        connection = mail.get_connection()
        connection.open()

        for obj in queryset:
            user = User.objects.filter(email=obj.sender_email)[0]
            if user.warnings < 2:
                html_message = loader.render_to_string('chat/warning.html', {'user_name': user.user_name})
                html_message = strip_tags(html_message)
                subject = "אזהרה על תוכן פוגעני"
                user.warnings += 1
                user.save()
            elif user.warnings == 2 :
                html_message = loader.render_to_string('chat/blocked.html', {'user_name': user.user_name})
                html_message = strip_tags(html_message)
                subject = "חסימה מאתר B7Fun"
                user.warnings += 1
                user.blocked = True
                user.save()

            email = mail.EmailMessage(
                subject,
                html_message,
                'b7funservice@gmail.com',
                [user.email],
                connection=connection,
            )
            email.send()

            # delete message
            ChatMessage.objects.filter(message_id=obj.abusive_message_id)[0].delete()

            # delete marked as abusive message
            obj.delete()

    actions = ['mark_as_abusive', mark_as_nonabusive]
    mark_as_abusive.short_description = "Mark message as abusive"
    mark_as_nonabusive.short_description = "Mark message as nonabusive"
