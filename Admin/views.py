from django.shortcuts import render
from .models import AdminModel

from .serializers import AdminSerializer
# Create your views here.

from rest_framework import generics
from .permissions import IsOwnerPermission
from rest_framework.permissions import IsAuthenticated

class AllAdminView(generics.ListCreateAPIView):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsOwnerPermissions,)

class RUDAdminView(generics.RetrieveUpdateDestroyAPIView):
     queryset = AdminModel.objects.all()
     serializer_class = AdminSerializer 
     permission_classes = (IsOwnerPermissions,)


