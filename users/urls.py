from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/add/', views.addUser, name='addUser'),
    path('', views.users, name='users'),
]