# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ
# pylint: disable=expression-not-assigned

from django.contrib import admin
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.utils.html import strip_tags
from django.template import loader
from django.core import mail
from .models import User, Emails
from .forms import EmailForm


admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ("date_joined", 'last_login', 'warnings', 'blocked')
    list_display = ("email", "user_name", "first_name", "last_name", 'warnings', 'blocked')
    fieldsets = (
        (None, {
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'about', 'profile_image', 'warnings', 'blocked')
        }),
    )
    search_fields = ['first_name', 'last_name']

    def send_mail(self, request, queryset):
        if 'apply' in request.POST:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                connection = mail.get_connection()
                connection.open()

                for user in queryset:
                    newemail = Emails()
                    newemail.subject = email_form.cleaned_data['subject']
                    newemail.content1 = email_form.cleaned_data['content']

                    email1 = mail.EmailMessage(
                        email_form.cleaned_data['subject'],
                        email_form.cleaned_data['content'],
                        'b7funservice@gmail.com',
                        [user.email],
                        connection=connection,
                    )
                    email1.send()
                    newemail.sent = str(user.email)
                    newemail.save()
                self.message_user(request, "Sent mail to {} users".format(queryset.count()))
                return HttpResponseRedirect(request.get_full_path())
        return render(request, 'accounts/admin/send_mail.html', context={'users':queryset, 'form':EmailForm()})

    def block_users(self, request, queryset):
        self.message_user(request, "Blocked {} users".format(queryset.count()))
        connection = mail.get_connection()
        connection.open()
        for obj in queryset:
            if not obj.blocked:
                html_message = loader.render_to_string('accounts/blocked.html', {'user_name': obj.user_name})
                html_message = strip_tags(html_message)
                obj.blocked = True
                [s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_id') == str(obj.id)]
                obj.save()
                email = mail.EmailMessage(
                    'חסימה מאתר B7Fun',
                    html_message,
                    'b7funservice@gmail.com',
                    [obj.email],
                    connection=connection,
                )
                email.send()

    def unblock_users(self, request, queryset):
        self.message_user(request, "Unblocked {} users".format(queryset.count()))
        connection = mail.get_connection()
        connection.open()
        for obj in queryset:
            if obj.blocked:
                html_message = loader.render_to_string('accounts/unblocked.html', {'user_name': obj.user_name})
                html_message = strip_tags(html_message)
                obj.blocked = False
                obj.save()
                email = mail.EmailMessage(
                    'הסרת חסימה מאתר B7Fun',
                    html_message,
                    'b7funservice@gmail.com',
                    [obj.email],
                    connection=connection,
                )
                email.send()

    actions = ['send_mail', 'block_users', 'unblock_users']
    send_mail.short_description = "Send Email"
    block_users.short_description = "Block Users"
    unblock_users.short_description = "Unblock Users"

@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    model = Emails
    list_display = ("subject", "content", "sent")
    list_filter = ("subject", 'sent')
    fieldsets = (
        (None, {
            'fields': ('sent', 'subject', 'content1')
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
