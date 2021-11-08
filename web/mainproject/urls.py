from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('main/', include('mainapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
]
