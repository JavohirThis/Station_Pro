from rest_framework import serializers
from .models import (UserModel, BronModel)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class BronSerializer(serializers.ModelSerializer):
    class Meta:
        model = BronModel
        fields = '__all__'
        