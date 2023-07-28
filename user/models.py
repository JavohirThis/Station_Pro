from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
# from admin.models import AdminModel
# from station.models import StationModel

class UserModel(models.Model):
    frist_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    phone = models.CharField(max_length=122)
    def __str__(self) -> str:
        return self.frist_name
    
    class Meta:
        db_table = 'user'

class BronModel(models.Model):

    station_fk = models.ForeignKey('station.StationModel', on_delete=models.SET_NULL,null=True)
    user_fk = models.ForeignKey(UserModel, on_delete=models.SET_NULL,null=True)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('o','owner'),
        ('u','user'),
    )

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)