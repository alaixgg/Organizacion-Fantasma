from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import user, Department
from .serializers import UserSerializer, DepartmentSerializer
from rest_framework.response import Response

def index(request):
    return HttpResponse("<h1>Hello world</h1>")

# Users
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Departments
class DepartmentCreateAPIView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Department deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
