# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring


from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('accounts.urls')),
    path('feed/', include('feed.urls')),
    path('admin/', admin.site.urls),
    path('Profile/', include('Profile.urls')),
    path('posts/', include('postsFeed.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', email_template_name="accounts/password_reset_email.html"),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
