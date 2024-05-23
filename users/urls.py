from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/add/', views.addUser, name='addUser'),
    path('users/edit/<int:user_id>/', views.editUser, name='editUser'),
    path('', views.users, name='users'),
]