from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', include('accounts.urls')),
<<<<<<< HEAD
=======
<<<<<<< HEAD
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
=======
>>>>>>> c4b52cab584890d65a65c4237d8b783d541d082f
    path('feed/', include('feed.urls')),
    path('admin/', admin.site.urls),
    path('Profile/', include('Profile.urls')),
<<<<<<< HEAD
=======
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('posts/', include('postsFeed.urls')),
=======
    path('admin/',admin.site.urls)
>>>>>>> 974b9cc65100a6d043a40be1c6b779051feccb74

>>>>>>> d4bfb58a561f3aee85694d9435e528044a5d83fb
>>>>>>> c4b52cab584890d65a65c4237d8b783d541d082f
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
