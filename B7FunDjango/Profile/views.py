from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UpdateProfileImage, UpdateUserDetails
from accounts.models import User
import os


@login_required(login_url='/')
def myProfile(request, err=None):
    UpdateProfileImageForm = UpdateProfileImage()
    changePasswordForm = form = PasswordChangeForm(request.user)
    changePasswordForm.fields['old_password'].widget.attrs.update({'class': 'form-control'})
    changePasswordForm.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
    changePasswordForm.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
    UpdateUserDetailsForm = UpdateUserDetails(initial={'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name,
        'user_name': request.user.user_name, 'about': request.user.about})
    return render(request, 'Profile/myProfile.html', {'VMuser': User.objects.get(email=request.user.email), "UpdateProfileImageForm": UpdateProfileImageForm,
    "UpdateUserDetailsForm": UpdateUserDetailsForm, "changePasswordForm": changePasswordForm, "errors": err})


