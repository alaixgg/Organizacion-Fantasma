from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

class user(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    salary = models.IntegerField()
    info = models.CharField(max_length=180)
    age = models.IntegerField(blank=False, null=False)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    balance = models.IntegerField()
