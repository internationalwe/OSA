from django.urls import path
from . import views

urlpatterns = [
    path('', views.sub, name='sub'),
    path('<int:sub_id>/', views.sub_index, name='sub_index'),
]
