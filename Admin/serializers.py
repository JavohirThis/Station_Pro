from rest_framework import serializers
from .models import AdminModel

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = '__all__'




    
