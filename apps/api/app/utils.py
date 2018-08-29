from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

SAFE_METHODS = ['GET', 'POST', 'HEAD', 'OPTIONS']
OBJECT_METHODS = ['GET', 'HEAD', 'OPTIONS']


class LoginPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS and
                request.user and
                request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id

