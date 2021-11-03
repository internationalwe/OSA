from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main/', include('mainapp.urls')),
    path('company/', include('cmpapp.urls')),
    path('admin/', admin.site.urls),
]
