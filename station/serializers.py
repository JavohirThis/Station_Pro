from rest_framework import serializers
from .models import StationModel

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        fields = '__all__'