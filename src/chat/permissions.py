from rest_framework import permissions
from .models import Chat


class IsInChat(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if Chat.objects.filter(users=request.user, id=obj.id).exists():
            return True

        return request.user.is_staff

