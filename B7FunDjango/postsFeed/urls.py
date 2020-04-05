from django.urls import path, include
from . import views

app_name = 'postsFeed'

urlpatterns = [
    path('', views.posts, name='posts'),
]