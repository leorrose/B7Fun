# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from .models import User


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(label='שם פרטי', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='שם משפחה', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(label='שם משתמש', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='דוא"ל', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='סיסמא', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='וודא סיסמא', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='ספר על עצמך', widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_image = forms.ImageField(label='תמונת פרופיל', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ('email', 'user_name')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error("confirm_password", forms.ValidationError("Confirm password does not match"))
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if len(qs) > 0:
            self.add_error("email", forms.ValidationError("This email is already registered"))
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(user_name=user_name)
        if len(qs) > 0:
            self.add_error("user_name", forms.ValidationError('This user name is already registered'))
        return user_name

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data['password']
        if password:
            try:
                validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password', error)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='דוא"ל', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(label='סיסמא', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError('User does not exist'))
            return None
        if not check_password(password, user.password) and password != user.password:
            self.add_error("password", forms.ValidationError('Password does not match user'))
            return None
        return self.cleaned_data

class EmailForm(forms.Form):
    subject = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'my-text-input', 'placeholder':'Subject'}))
    content = forms.CharField(label="", required=True, widget=forms.Textarea(
        attrs={'class': 'my-text-area', 'placeholder':'Content', 'rows': '30'}))
