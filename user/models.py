from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from datetime import datetime
# Create your models here.
# from admin.models import AdminModel
# from station.models import StationModel


class UserModel(models.Model):
    frist_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    phone = PhoneNumberField()


class BronModel(models.Model):
    # station_fk = models.ForeignKey()
    user_fk = models.ForeignKey(UserModel, on_delete=models.SET_NULL,null=True)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
