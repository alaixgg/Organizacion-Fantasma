from django.db import models
from CRUD.models import user
from django.utils import timezone

class Payroll(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    salary = models.IntegerField()
    payment_date = models.DateTimeField(default=timezone.now)
    pay = models.IntegerField()
    

    def __str__(self):
        return f"Si hizo el pago de nomina a {self.user.name}{self.user.last_name} por {self.pay}, el saldo de su cuenta es de {self.user.balance} "
    
