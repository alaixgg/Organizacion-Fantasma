from django.shortcuts import render
from CRUD.models import user
from .models import Payroll, verification
from datetime import datetime, time
from django.utils import timezone

# Create your views here.
def pay_salaries():
    
    now = timezone.localtime(timezone.now())

    
    if now.hour == 18:  
        user.balace= user.salary+user.balance
        verification.pay = True #esto para enviar los correos

