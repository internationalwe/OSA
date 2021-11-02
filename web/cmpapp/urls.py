from django.urls import path
from . import views

app_name = 'cmpapp'
urlpatterns = [
    path('', views.cmplist, name='cmplist'),
    path('<int:company_id>/', views.cmp, name='cmp'),
]