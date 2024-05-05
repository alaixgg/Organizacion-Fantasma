from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import user
from .serializers import UserSerializer

def index(request):
    #Logica 
    return HttpResponse("<h1>Hello world</h1>")

class UserListCreate(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer