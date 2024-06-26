from rest_framework.permissions import BasePermission
from users.models import UserRole, User


class IsModerator(BasePermission):
    message = "Вы не модератор!"

    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False


class IsUser(BasePermission):
    message = "Вы не можете редактировать чужой профиль!"

    def has_permission(self, request, view):
        if request.user.pk == User.pk:
            return True
        return False
