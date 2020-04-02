from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout
from .forms import LoginForm
from .models import User


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