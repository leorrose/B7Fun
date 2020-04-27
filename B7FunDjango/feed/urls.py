from django.urls import path,include
from . import views


app_name = 'feed'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('filter/<str:searchTerm>', views.filter, name='filter'),
]