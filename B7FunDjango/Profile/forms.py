from django import forms
from accounts.models import User
from django.contrib.auth.hashers import check_password

class UpdateProfileImage(forms.Form):
    profile_image = forms.ImageField(label='תמונת פרופיל', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

class UpdateUserDetails(forms.Form):
    first_name = forms.CharField(label='שם פרטי', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='שם משפחה',widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(label='שם משתמש',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='דוא"ל', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='ספר על עצמך', widget=forms.Textarea(attrs={'class': 'form-control'}))
    