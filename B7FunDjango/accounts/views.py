# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from .forms import SignUpForm, LoginForm
from .models import User, Logins


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            about = form.cleaned_data.get('about')
            profile_image = form.cleaned_data.get('profile_image')
            if not profile_image:
                profile_image = 'default_profile.png'
            new_user = User.objects.create_user(email=email,
                                                user_name=user_name,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                about=about,
                                                profile_image=profile_image)
            max_id = Logins.objects.all().order_by('id').last()
            max_id = max_id.id if max_id else -1
            Logins.objects.create(id=max_id+1, user_email=email, login_month=datetime.now().month, login_year=datetime.now().year)
            login(request, new_user)
            return redirect('feed:feed')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin:login')
        return redirect('feed:feed')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email,)
            if not user.blocked:
                login(request, user)
                if user.is_admin:
                    return redirect('admin:index')
                max_id = Logins.objects.all().order_by('id').last()
                max_id = max_id.id if max_id else -1
                Logins.objects.create(id=max_id+1, user_email=user.email, login_month=datetime.now().month, login_year=datetime.now().year)
                return redirect('feed:feed')
            form.add_error(None, ValidationError("User is blocked"))
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
