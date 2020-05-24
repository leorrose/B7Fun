# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unnecessary-lambda

import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.cache import cache
from PIL import Image
from accounts.models import User
from chat.models import ChatMessage, AbusiveChatMessage
from .forms import UpdateProfileImage, UpdateUserDetails


@login_required(login_url='/')
def my_profile(request, err=None):
    update_profile_image_form = UpdateProfileImage()
    change_password_form = PasswordChangeForm(request.user)
    change_password_form.fields['old_password'].widget.attrs.update(
        {'class': 'form-control'})
    change_password_form.fields['new_password1'].widget.attrs.update(
        {'class': 'form-control'})
    change_password_form.fields['new_password2'].widget.attrs.update(
        {'class': 'form-control'})
    update_user_details_form = UpdateUserDetails(
        initial={'email': request.user.email, 'first_name': request.user.first_name,
                 'last_name': request.user.last_name,
                 'user_name': request.user.user_name, 'about': request.user.about})
    return render(request, 'Profile/my_profile.html',
                  {'VMuser': User.objects.get(email=request.user.email),
                   "UpdateProfileImageForm": update_profile_image_form,
                   "UpdateUserDetailsForm": update_user_details_form,
                   "changePasswordForm": change_password_form, "errors": err})


@login_required(login_url='/')
def edit_profile_image(request):
    if request.method == 'POST':
        form = UpdateProfileImage(request.POST, request.FILES)
        if form.is_valid():
            if request.user.profile_image and request.user.profile_image.name !=\
                    "default_profile.png" and os.path.exists(request.user.profile_image.path):
                os.remove(request.user.profile_image.path)
            if form.cleaned_data.get('profile_image'):
                request.user.profile_image = form.cleaned_data.get(  # pragma: no cover
                    'profile_image')
            else:
                request.user.profile_image = "default_profile.png"
            request.user.save()
        else:
            error_message = [] if form.errors == {} else list(
                map(lambda x: "".join(x), form.errors.values()))
            error_message += [] if form.non_field_errors else list(
                map(lambda x: "".join(x), form.non_field_errors.values()))
            return redirect('Profile:my_profile', err=", ".join(error_message))
    return redirect('Profile:my_profile')


@login_required(login_url='/')
def edit_user_details(request):
    if request.method == 'POST':
        form = UpdateUserDetails(request.POST)
        if form.is_valid():
            error_message = [] if form.errors == {} else [form.errors.values()]
            if(form.cleaned_data.get('user_name') != request.user.user_name and
               len(User.objects.filter(user_name=form.cleaned_data.get('user_name'))) > 0):
                error_message.append("user name already exists, please choose different user name")
            else:
                request.user.user_name = form.cleaned_data.get('user_name')

            if(form.cleaned_data.get('email') != request.user.email and
               len(User.objects.filter(email=form.cleaned_data.get('email'))) > 0):
                error_message.append("user email already exists, please choose different email")
            else:
                ChatMessage.objects.filter(sender_email=request.user.email).update(sender_email=form.cleaned_data.get('email'))
                AbusiveChatMessage.objects.filter(sender_email=request.user.email).update(sender_email=form.cleaned_data.get('email'))
                request.user.email = form.cleaned_data.get('email')

            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.about = form.cleaned_data.get('about')
            request.user.save()

            if error_message != []:
                return redirect('Profile:my_profile', err=", ".join(error_message))
        else:
            error_message = [] if form.errors == {} else list(
                map(lambda x: "".join(x), form.errors.values()))
            error_message += [] if form.non_field_errors else list(
                map(lambda x: "".join(x), form.non_field_errors.values()))
            return redirect('Profile:my_profile', err=", ".join(error_message))
    return redirect('Profile:my_profile')


@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('Profile:my_profile')
        error_message = [] if form.errors == {} else list(
            map(lambda x: "".join(x), form.errors.values()))
        error_message += [] if form.non_field_errors else list(
            map(lambda x: "".join(x), form.non_field_errors.values()))
        return redirect('Profile:my_profile', err=", ".join(error_message))
    return redirect('Profile:my_profile')


@login_required(login_url='/')
def rotate_pic(request):
    if request.user.profile_image and request.user.profile_image.name != \
            "default_profile.png" and os.path.exists(request.user.profile_image.path):
        img = Image.open(request.user.profile_image.path)
        img = img.rotate(90, expand=False, fillcolor='white')
        img.save(request.user.profile_image.path)
        cache.clear()
    return redirect('Profile:my_profile')

@login_required(login_url='/')
def show_user_profile(request, user_email=None):
    return render(request, 'Profile/view_profile.html', {'VMuser': User.objects.get(email=user_email)})
