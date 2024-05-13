from rest_framework.permissions import BasePermission


class IsActiveModer(BasePermission):
    message = "Ошибка! Доступ разрешен только активным сотрудникам!"

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff and request.user.is_active
