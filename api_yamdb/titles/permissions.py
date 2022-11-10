from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Администратор'."""

    message = 'Изменение чужого контента запрещено!'
    access_roles = ('admin',)

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.is_authenticated and
            request.user.role in self.access_roles or
            request.user.is_superuser
        )
