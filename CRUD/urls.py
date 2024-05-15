from django.contrib import admin
from django.urls import path
from .views import (
    UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,
    DepartmentCreateAPIView, DepartmentListAPIView, DepartmentRetrieveUpdateDestroyAPIView,
    index
)

urlpatterns = [
    path('', index),
    # User endpoints
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create-api'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy-api'),
    # Department endpoints
    path('api/departments/', DepartmentCreateAPIView.as_view(), name='department-create-api'),
    path('api/departments/list/', DepartmentListAPIView.as_view(), name='department-list-api'),
    path('api/departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-retrieve-update-destroy-api'),
]
