# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views


app_name = 'reports'

urlpatterns = [
    path('', views.report, name='report'),
]
