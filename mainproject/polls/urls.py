from django.urls import path
from . import views

urlpatterns = [
    path('', views.polls_list, name='polls_list'),
    path('polls_if/', views.polls_if, name='polls_if'),
    path('<int:question_id>/', views.polls_vote, name='polls_vote'),
]
