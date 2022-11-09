from rest_framework import permissions

ADMINS = ['admin']


class IsAuthenticatedAdmin(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Администратор'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role in ADMINS or request.user.is_superuser
        )
