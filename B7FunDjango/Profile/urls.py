from django.urls import path,include
from . import views


app_name = 'Profile'

urlpatterns = [
    # path('myProfile', views.myProfile, name='myProfile'),
    path('editProfile', views.editProfile, name='editProfile')
]