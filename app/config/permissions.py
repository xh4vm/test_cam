from rest_framework.permissions import BasePermission


class UnauthenticatedPOST(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['POST']
