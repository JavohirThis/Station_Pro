from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# Create your models here.
class StationModel(models.Model):
    name = models.CharField(max_length=100, default='')
    admin = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True)
    phone_number = PhoneNumberField(blank = True)
    email = models.EmailField(max_length=100, blank= True, unique=True)
    adress = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='images/')
    hourprice = models.PositiveSmallIntegerField()
    info = models.CharField(max_length=3000)
    def __str__(self) -> str:
        return self.image.name
class Meta:
    db_table = 'station'