from django.contrib import admin
from .models import UserModel, BronModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(BronModel)