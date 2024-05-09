from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from .models import user
from .serializers import UserSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics, status
from rest_framework.response import Response

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
    
    
    def __str__(self):
        return f'{self.name} {self.last_name}'
    
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    # Override para personalizar la respuesta de eliminación
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)