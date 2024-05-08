from django.http import HttpResponse
from rest_framework import generics
from .models import user
from .models import Department
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .serializers import UserSerializer

def index(request):
    #Logica 
    return HttpResponse("<h1>Hello world</h1>")

class UserListCreate(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    
class UserListView(ListView):
    model = user
    template_name = 'user_list.html'

class UserCreateView(CreateView):
    model = user
    fields = ['name', 'last_name', 'age']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = user
    fields = ['name', 'last_name', 'age']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = user
    success_url = reverse_lazy('user_list')
    
#Departaments
class DepartamentsListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = UserSerializer
    
class DepartamentsListView(ListView):
    model = Department
    template_name = 'department_list.html'

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name']
    template_name = 'Department_form.html'
    success_url = reverse_lazy('Department_list')

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['name']
    template_name = 'Department_form.html'
    success_url = reverse_lazy('Department_list')

class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = reverse_lazy('Department_list')