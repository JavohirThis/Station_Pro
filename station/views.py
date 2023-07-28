from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import StationModel
from .serializer import StationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerpermission

class StationView(generics.ListCreateAPIView):
    queryset = StationModel.objects.all()
    serializer_class = StationSerializer

class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StationModel.objects.all()
    serializer_class = StationSerializer