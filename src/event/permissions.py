from rest_framework import permissions
from .models import EventModel
from django.db.models import Q


class CanSeeEvent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        TODO:
         не понимаю((
        """

        return request.user.is_staff
