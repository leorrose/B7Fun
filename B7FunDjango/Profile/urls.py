# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views


app_name = 'Profile'

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile'),
    path('my_profile/<str:err>/', views.my_profile, name='my_profile'),
    path('edit_profile_image/', views.edit_profile_image, name='edit_profile_image'),
    path('edit_user_details/', views.edit_user_details, name='edit_user_details'),
    path('change_password/', views.change_password, name='change_password'),
    path('rotate_pic/', views.rotate_pic, name='rotate_pic'),
    path('show_user_profile/', views.show_user_profile, name='show_user_profile_no_arg'),
    path('show_user_profile/<str:user_email>', views.show_user_profile, name='show_user_profile')
]
