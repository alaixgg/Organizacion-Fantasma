from django.db import models
from CRUD.models import user, email

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    check = models.BooleanField(default=False)

