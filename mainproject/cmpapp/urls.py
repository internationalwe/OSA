from django.urls import path
from . import views

urlpatterns = [
    path('', views.cmplist, name='cmplist'),
    path('<int:company_id>/', views.cmp, name='cmp'),
]