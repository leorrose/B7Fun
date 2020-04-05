from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(label='שם פרטי', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='שם משפחה',widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_name = forms.CharField(label='שם משתמש',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='דוא"ל', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='סיסמה',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='וודא סיסמה',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='ספר על עצמך', widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_image = forms.ImageField(label='תמונת פרופיל', required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ('email', 'user_name')

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError({"confirm_password":"Confirm password does not match"})
        if len(password) < 4:
            raise forms.ValidationError({"password": "Invalid password - minimum length 4"})
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if len(qs) > 0:
            raise forms.ValidationError("This email is already registered")
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(user_name=user_name)
        if len(qs) > 0:
            raise forms.ValidationError('This user name is already registered')
        return user_name

    def save(self, commit=True):
        user = super(SignUpForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='דוא"ל', widget=forms.TextInput(attrs={'placeholder' : 'Email', 'class': 'form-control'}))
    password = forms.CharField(label='סיסמה', widget=forms.PasswordInput(attrs={'placeholder' : 'Password' , 'class': 'form-control'}))

    def clean(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        if not check_password(password, user.password) and password != user.password:
            raise forms.ValidationError({"password": "Password does not match user"})
        return self.cleaned_data


