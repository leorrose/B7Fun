# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views

app_name = 'postsFeed'

urlpatterns = [
    path('', views.admin_posts, name='admin_posts'),
]
