from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('accounts.urls')),
<<<<<<< HEAD
    path('feed/', include('feed.urls')),
    path('posts/', include)('postsFeed.urls'),
=======
    path('admin/', include('accounts.urls')),
    path('feed/', include('feed.urls')),
    path('Profile/', include('Profile.urls'))
    path('admin/',admin.site.urls)
>>>>>>> 685cfc790247377a56223a57ee799e16682e2c96
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)