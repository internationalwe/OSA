from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', include('mainapp.urls')),
    path('sub/', include('subapp.urls')),
    path('admin/', admin.site.urls),
]
