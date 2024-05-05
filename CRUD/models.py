from django.db import models
from django.utils import timezone


# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False, null=False)

    
    def __str__(self):
        return f'{self.name} {self.last_name}'