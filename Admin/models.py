from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('u','user')
    )
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

# Create your models here.
class AdminModel(models.Model):
    firts_name=models.CharField(max_length=65, default='')
    last_name=models.CharField(max_length=65, default='')
    phone= models.CharField(max_length=122)
    email=models.EmailField(max_length=100 ,unique=True)
    image=models.ImageField(max_length=200 ,upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        db_table='Admin'