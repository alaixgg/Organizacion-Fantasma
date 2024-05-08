from django.shortcuts import render
from CRUD.models import user
from .models import Payroll
from datetime import datetime, time
from django.utils import timezone

# Create your views here.
def pay_salaries():
    
    now = timezone.localtime(timezone.now())

    
    if now.hour == 18:  
        user.balace= user.salary+user.balance




###
def update_balance(employee_id, payment_amount):
    # Buscar el registro de nómina del empleado
    payroll_record = Payroll.objects.get(user_id=employee_id)

    # Sumar el pago al saldo actual del empleado
    payroll_record.user.balance += payment_amount

    # Guardar el cambio en el saldo del empleado
    payroll_record.user.save()

    # Devolver el nuevo saldo actualizado
    return payroll_record.user.balance