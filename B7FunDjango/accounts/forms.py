from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        try:                                       #לבדוק אם צריך לשנות
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        if not check_password(password, user.password) and password != user.password:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data