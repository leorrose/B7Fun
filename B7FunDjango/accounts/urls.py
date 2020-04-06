from django.urls import path,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name="signup"),
    path('logout',views.logout_view,name='logout'),

]
