# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views


app_name = 'feed'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('filter_data/<str:search_term>',
         views.filter_data, name='filter_data'),
]
