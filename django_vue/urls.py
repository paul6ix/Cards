from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vi', include('djoser.urls')),
    path('api/v2', include('djoser.urls.authtoken'))
]