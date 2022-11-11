from rest_framework import permissions

ADMINS = ['admin']


class IsAuthenticatedAdmin(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Администратор'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role in ADMINS or request.user.is_superuser
        )


class IsAuthorOrHiAccessOrReadOnly(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Автор_Или_Его_Роль_Разрешена'."""

    message = 'Изменение чужого контента запрещено!'
    access_roles = ('moderator', 'admin')

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.role in self.access_roles
                or request.user.is_superuser)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Администратор'."""

    message = 'Изменение чужого контента запрещено!'
    access_roles = ('admin',)

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.role in self.access_roles
            or request.user.is_superuser
        )
