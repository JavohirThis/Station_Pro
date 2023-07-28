from django.contrib import admin

# Register your models here.
from .models import AdminModel, CustomerUser

admin.site.register(AdminModel)
admin.site.register(CustomerUser)