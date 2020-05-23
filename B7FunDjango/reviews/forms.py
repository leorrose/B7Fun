# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django import forms


class ReviewForm(forms.Form):
    review_content = forms.CharField(label='תגובה', widget=forms.Textarea(
        attrs={'class': 'form-control', 'dir': 'rtl', 'placeholder': 'כתוב תגובה'}))
    rating = forms.IntegerField(label='דרג')


