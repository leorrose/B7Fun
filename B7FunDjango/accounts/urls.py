from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/signup', views.signup_view, name="signup"),
    path('accounts/logout',views.logout_view,name='logout'),

]
