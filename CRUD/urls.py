from django.contrib import admin
from django.urls import path
from .views import UserCreateView, UserDeleteView, UserUpdateView, UserListCreate, index 
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', index),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),  
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
]