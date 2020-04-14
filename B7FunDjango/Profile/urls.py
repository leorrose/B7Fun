from django.urls import path,include
from . import views


app_name = 'Profile'

urlpatterns = [
    path('myProfile', views.myProfile, name='myProfile'),
    path('myProfile/<str:err>', views.myProfile, name='myProfile'),
    path('editProfileImage', views.editProfileImage, name='editProfileImage'),
    path('editUserDetails', views.editUserDetails, name='editUserDetails'),
    path('change_password', views.change_password, name='change_password'),
    path('rotatePic', views.rotatePic, name='rotatePic')
]