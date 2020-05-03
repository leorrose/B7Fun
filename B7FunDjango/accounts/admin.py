# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-argument
# pylint: disable=arguments-differ

from django.contrib import admin
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import mail
from .models import User, Emails
from .forms import EmailForm


admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_filter = ("date_joined", 'last_login')
    list_display = ("email", "user_name", "first_name", "last_name")
    fieldsets = (
        (None, {
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'about', 'profile_image')
        }),
    )
    search_fields = ['first_name', 'last_name']

    def send_mail(self, request, queryset):
        if 'apply' in request.POST:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                connection = mail.get_connection()
                connection.open()

                newemail = Emails()
                flag = 0
                emails = ""
                newemail.subject = email_form.cleaned_data['subject']
                newemail.content = email_form.cleaned_data['content']

                if queryset.count() == User.objects.all().count():
                    newemail.sent = "sent to all users"
                    flag = 1

                for user in queryset:
                    email1 = mail.EmailMessage(
                        email_form.cleaned_data['subject'],
                        email_form.cleaned_data['content'],
                        'b7funservice@gmail.com',
                        [user.email],
                        connection=connection,
                    )
                    email1.send()
                    if flag == 0:
                        emails = emails+str(user.email)+" "

                if flag == 0:
                    newemail.sent = emails

                newemail.save()
                self.message_user(request, "Sent mail to {} users".format(queryset.count()))
                return HttpResponseRedirect(request.get_full_path())
        return render(request, 'accounts/admin/send_mail.html', context={'users':queryset, 'form':EmailForm()})

    actions = ['send_mail']
    send_mail.short_description = "Send Email"

@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    list_display = ("subject", "truncated_name", "sent")
    list_filter = ("subject", 'sent')
    fieldsets = (
        (None, {
            'fields': ('sent', 'subject', 'content')
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
