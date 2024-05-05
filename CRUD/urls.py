from django.contrib import admin
from django.urls import path

from .views import index 
from .views import UserListCreate

urlpatterns = [
    path('', index),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
]
