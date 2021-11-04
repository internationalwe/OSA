from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('main/', include('mainapp.urls')),
    path('sub/', include('subapp.urls')),
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('', views.main, name='main'),
]
