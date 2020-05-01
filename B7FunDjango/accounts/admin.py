# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.core import mail
from .forms import EmailForm


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

    def send_mail(self, request, queryset):
        if 'apply' in request.POST:
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                connection = mail.get_connection()
                connection.open()

                for user in queryset:
                    email1 = mail.EmailMessage(
                        email_form.cleaned_data['subject'],
                        email_form.cleaned_data['content'],
                        'b7funservice@gmail.com',
                        [user.email],
                        connection=connection,
                    )
                    email1.send()
                self.message_user(request, "Sent mail to {} users".format(queryset.count()))
                return HttpResponseRedirect(request.get_full_path())
        return render(request, 'accounts/admin/send_mail.html', context={'users':queryset, 'form':EmailForm()})

    actions = ['send_mail']
    send_mail.short_description = "Send Email"