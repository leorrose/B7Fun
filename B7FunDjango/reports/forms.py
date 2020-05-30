# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django import forms

ch = [
    ('מרכזים קהילתיים', 'מרכזים קהילתיים'),
    ('גינות כלבים', 'גינות כלבים'),
    ('ועדונים חברתיים לקשיש', 'מועדונים חברתיים לקשיש'),
    ('מתקני משחק', 'מתקני משחק'),
    ('מתקני ספורט', 'מתקני ספורט'),
    ('אתרי טבע עירוניים', 'אתרי טבע עירוניים'),
    ('אחר', 'אחר')
]

class ReportsForm(forms.Form):
    subject = forms.CharField(label='נושא', required=True, widget=forms.Select(
        choices=ch, attrs={'class': 'form-control', 'dir': 'rtl', 'placeholder': 'כתוב נושא'}))
    content = forms.CharField(label='דיווח', required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'dir': 'rtl', 'placeholder': 'משהו שתרצה/י לדווח?'}))
