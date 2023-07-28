from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerpermission
from rest_framework.permissions import BasePermission 

class IsOwnerpermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.Admin == obj.Admin