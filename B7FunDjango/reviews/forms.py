# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ReviewForm(forms.Form):
    review_content = forms.CharField(label='תגובה', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'dir': 'rtl', 'placeholder': 'משהו שתרצה/י לכתוב?'}))
    rating = forms.IntegerField(label='דרג', required=True,
                                validators=[MaxValueValidator(5), MinValueValidator(1)], initial=5)
