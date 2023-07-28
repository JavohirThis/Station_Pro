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
    TIME_CHOICES = [
        ('08:00', '09:00'),
        ('09:00', '10:00'),
        ('10:00', '11:00'),
        ('11:00', '12:00'),
        ('12:00', '13:00'),
        ('13:00', '14:00'),
        ('14:00', '15:00'),
        ('15:00', '16:00'),
        ('16:00', '17:00'),
        ('17:00', '18:00'),
        ('18:00', '19:00'),
        ('19:00', '20:00'),
        ('20:00', '21:00'),
        ('21:00', '22:00'),
        ('22:00', '23:00'),
        ('23:00', '00:00'),
        ('00:00', '01:00'),
    ]
    time = models.CharField(max_length=6, choices=TIME_CHOICES)
    status = models.BooleanField(default=False)
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('o','owner'),
        ('u','user'),
    )

    

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)