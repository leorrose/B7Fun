from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, LoginForm
from .models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            about = form.cleaned_data.get('about')
            profile_image = form.cleaned_data.get('profile_image')
            new_user = User.objects.create_user(email=email,
                                                user_name=user_name,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                about=about,
                                                profile_image=profile_image)
            login(request, new_user)
            return redirect('feed:feed')
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
            if user.is_admin:
                return redirect('admin:index')
            return redirect('feed:feed')
    else:
        form = LoginForm()
    return render(request,'accounts/login.html', {'form':form})


def logout_view(request):
<<<<<<< HEAD
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

=======
    logout(request)
    return redirect('accounts:login')
>>>>>>> d4bfb58a561f3aee85694d9435e528044a5d83fb
