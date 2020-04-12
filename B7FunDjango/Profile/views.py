from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UpdateProfileImage, UpdateUserDetails
from accounts.models import User
import os
from PIL import Image


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

@login_required(login_url='/')
def editProfileImage(request):
    if request.method == 'POST':
        form = UpdateProfileImage(request.POST, request.FILES)
        if form.is_valid():
            if request.user.profile_image and os.path.isfile(request.user.profile_image.path):
                os.remove(request.user.profile_image.path)
            request.user.profile_image = form.cleaned_data.get('profile_image')
            request.user.save()
        else:
            errorMessage = [] if form.errors=={} else list(map(lambda x: "".join(x) , form.errors.values()))
            errorMessage += [] if form.non_field_errors else list(map(lambda x: "".join(x) , form.non_field_errors.values()))
            return redirect('Profile:myProfile', err=", ".join(errorMessage))
    return redirect('Profile:myProfile')

@login_required(login_url='/')
def editUserDetails(request):
    if request.method == 'POST':
        form = UpdateUserDetails(request.POST)
        if form.is_valid():
            errorMessage = [] if form.errors=={} else [form.errors.values()]
            if( form.cleaned_data.get('user_name') != request.user.user_name and len(User.objects.filter(user_name=form.cleaned_data.get('user_name'))) > 0):
                errorMessage.append("user name already exists, please choose different user name")
            else:
                request.user.user_name = form.cleaned_data.get('user_name')

            if( form.cleaned_data.get('email') != request.user.email and len(User.objects.filter(email=form.cleaned_data.get('email'))) > 0):
                errorMessage.append("user email already exists, please choose different email")
            else:
                request.user.email = form.cleaned_data.get('email')

            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.about = form.cleaned_data.get('about')
            request.user.save()
            if errorMessage != []:
                return redirect('Profile:myProfile', err=", ".join(errorMessage))
        else:
            errorMessage = [] if form.errors=={} else list(map(lambda x: "".join(x) , form.errors.values()))
            errorMessage += [] if form.non_field_errors else list(map(lambda x: "".join(x) , form.non_field_errors.values()))
            return redirect('Profile:myProfile', err=", ".join(errorMessage))
    return redirect('Profile:myProfile')

@login_required(login_url='/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('Profile:myProfile')
        else:
            errorMessage = [] if form.errors=={} else list(map(lambda x: "".join(x) , form.errors.values()))
            errorMessage += [] if form.non_field_errors else list(map(lambda x: "".join(x) , form.non_field_errors.values()))
            return redirect('Profile:myProfile', err=", ".join(errorMessage))
    return redirect('Profile:myProfile')

@login_required(login_url='/')
def rotatePic(request):
    if request.user.profile_image and os.path.isfile(request.user.profile_image.path):
        img = Image.open(request.user.profile_image.path)
        img = img.rotate(90, expand=False, fillcolor='white')
        img.save(request.user.profile_image.path, "JPEG")
    return redirect('Profile:myProfile')