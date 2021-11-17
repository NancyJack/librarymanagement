from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as authentication_views
from library import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('library.urls')),
    path('',authentication_views.LoginView.as_view(template_name='library/login.html'),name='login'),
    
    path('logout/',authentication_views.LogoutView.as_view(template_name='library/logout.html'),name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
