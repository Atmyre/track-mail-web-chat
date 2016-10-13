from rest_framework import permissions
from .models import Chat


class IsInChat(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(Chat.objects.filter(chat_to_user__user=request.user, id=obj.id))
        print(Chat.objects.filter(chat_to_user__user=request.user))
        if Chat.objects.filter(users=request.user, id=obj.id).exists():
            return True

        return False
