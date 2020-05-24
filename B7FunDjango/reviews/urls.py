# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.review, name='review'),
    path('reviews_list', views.reviews_list, name='reviews_list'),
]
