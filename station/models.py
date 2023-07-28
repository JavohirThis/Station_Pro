from django.db import models
from datetime import datetime
from Admin.models import AdminModel
from user.models import UserModel
# Create your models here.
class StationModel(models.Model):
    admin = models.ForeignKey(AdminModel, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=100, default='')
    image =models.ImageField(max_length=200 ,upload_to='images/')
    hourprice = models.PositiveSmallIntegerField(default='')
    phone_number = models.CharField(max_length=122, default='')
    email = models.EmailField(max_length=100, blank= True)
    adress = models.CharField(max_length=200, default='')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, default=None)
 
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'station'