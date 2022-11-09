from rest_framework import permissions

ADMINS = ['admin', 'superuser']


class IsAuthenticatedAdmin(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Адмминистратор'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role in ADMINS or request.user.is_superuser
        )


class IsAdminPatchRequest(permissions.BasePermission):
    """Разрешение 'Если_Пользователь_Адмминистратор_и_запрос_PATCH'."""
    def has_permission(self, request, view):
        return request.method == "PATCH" and (
            request.user.role in ADMINS or request.user.is_superuser
        )
