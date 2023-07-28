from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from .permissions import IsOwnerpermission
from .models import (UserModel, BronModel)
from .serializers import (UserSerializer, BronSerializer)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerpermission,)


class BronListCreateView(generics.ListCreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated,)



class BronRUDView(generics.ListCreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsOwnerpermission,)

