from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if len(qs) > 0:
            raise forms.ValidationError('This email is already registered')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if len(qs) > 0:
            raise forms.ValidationError('This username is already registered')
        return username

    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        #user.is_active = False
        if commit:
            user.save()
        return user


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