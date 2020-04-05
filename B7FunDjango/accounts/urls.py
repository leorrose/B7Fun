from django.urls import path,include
from . import views
from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
<<<<<<< HEAD
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name="signup"),
    path('logout',views.logout_view,name='logout'),
]

=======
    # path('admin/', admin.site.urls),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/signup', views.signup_view, name="signup"),
    path('accounts/logout',views.logout_view,name='logout')
]
>>>>>>> d4bfb58a561f3aee85694d9435e528044a5d83fb
