from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/add/', views.addUser, name='addUser'),
    path('users/edit/<int:user_id>/', views.editUser, name='editUser'),
    path('users/delete/<int:user_id>/', views.users, name='users'),
    path('', views.users, name='users'),
]