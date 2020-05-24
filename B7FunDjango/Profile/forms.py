# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django import forms


class UpdateProfileImage(forms.Form):
    profile_image = forms.ImageField(label='תמונת פרופיל', required=False, widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))


class UpdateUserDetails(forms.Form):
    first_name = forms.CharField(label='שם פרטי', widget=forms.TextInput(attrs={'class': 'form-control', 'dir':'rtl'}))
    last_name = forms.CharField(label='שם משפחה', widget=forms.TextInput(attrs={'class': 'form-control', 'dir':'rtl'}))
    user_name = forms.CharField(label='שם משתמש', widget=forms.TextInput(attrs={'class': 'form-control', 'dir':'rtl'}))
    email = forms.EmailField(label='דוא"ל', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='ספר על עצמך', widget=forms.Textarea(attrs={'class': 'form-control', 'dir':'rtl'}))
