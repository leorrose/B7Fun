from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout
from .forms import SignUpForm, LoginForm
from .models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            new_user = User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
            login(request, new_user)
           # return redirect('dog_gardens:list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.get(email=email,)
            login(request, user)
           # return redirect('dog_gardens:list')
    else:
        form = LoginForm()
    return render(request,'accounts/login.html', {'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')