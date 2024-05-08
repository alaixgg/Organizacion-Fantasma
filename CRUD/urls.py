from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from .views import DepartamentsListCreate, DepartamentsListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView

urlpatterns = [
    # URLs para usuarios
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    
    # URLs para departamentos
    path('departments/', DepartamentsListView.as_view(), name='department-list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),
]
