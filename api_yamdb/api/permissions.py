from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Автор_Или_Его_Роль_Разрешена'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated
