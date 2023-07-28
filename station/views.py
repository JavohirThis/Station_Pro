from django.shortcuts import render
from .models import StationModel
from .serializers import StationSerializer
from rest_framework import generics

class StationnView(generics.ListCreateAPIView):
    queryset = StationModel.objects.all()
    serializer_class = StationSerializer
class StationRudView(generics.RetrieveUpdateDestroyAPIView):
     queryset = StationModel.objects.all()
     serializer_class = StationSerializer 

