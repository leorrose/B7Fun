from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout
from accounts.forms import SignUpForm
from accounts.models import User

def editProfile(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data.get('last_name')
            updateUser = User.objects.get(email=request.user.email)
            updateUser.email = form.cleaned_data.get('email')
            updateUser.username = form.cleaned_data.get('username')
            updateUser.password = form.cleaned_data.get('password1')
            updateUser.first_name = form.cleaned_data.get('first_name')
            updateUser.last_name = form.cleaned_data.get('last_name')
            updateUser.save()
            logout(request, request.user)
            login(request, updateUser)
            return redirect('Profile:myProfile')
    print(User.objects.get(email=request.user.email))
    form = SignUpForm(instance = User.objects.get(email=request.user.email))
    return render(request,'Profile/editProfile.html', {'form': SignUpForm})