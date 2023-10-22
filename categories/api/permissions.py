from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # All users and/or visitors have read permission
        if request.method == 'GET':
            return True
        # Only administrators have all permissions enabled
        return request.user.is_staff