# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ
# pylint: disable= expression-not-assigned

from django.contrib import admin
from django.template import loader
from django.core import mail
from django.utils.html import strip_tags
from django.contrib.sessions.models import Session
from accounts.models import User
from .models import ChatMessage, AbusiveChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ('date', 'sender_email', 'chat_room_type', 'chat_room_id')
    list_display = ('message', 'date', 'sender_email', 'chat_room_type', 'chat_room_id')
    fieldsets = (
        (None, {
            'fields': ('message', 'sender_email', 'chat_room_type', 'chat_room_id')
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
            user = User.objects.filter(email=obj.sender_email)
            if len(user) > 0:
                user = user[0]
            else:
                continue

            if user.warnings < 2:
                html_message = loader.render_to_string('chat/warning.html', {'user_name': user.user_name})
                html_message = strip_tags(html_message)
                subject = "אזהרה על תוכן פוגעני"
                user.warnings += 1
                user.save()
            elif user.warnings >= 2:
                html_message = loader.render_to_string('chat/blocked.html', {'user_name': user.user_name})
                html_message = strip_tags(html_message)
                subject = "חסימה מאתר B7Fun"
                user.warnings += 1
                user.blocked = True
                user.save()
                [s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_id') == str(user.id)]

            email = mail.EmailMessage(
                subject,
                html_message,
                'b7funservice@gmail.com',
                [user.email],
                connection=connection,
            )
            email.send()

            # delete message
            chat_message = ChatMessage.objects.filter(message_id=obj.abusive_message_id)
            if len(chat_message) == 1:
                chat_message[0].delete()

            # delete marked as abusive message
            obj.delete()

    actions = ['mark_as_abusive', 'mark_as_nonabusive']
    mark_as_abusive.short_description = "Mark message as abusive"
    mark_as_nonabusive.short_description = "Mark message as nonabusive"
