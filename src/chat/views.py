from django.shortcuts import render
from .models import Chat, ChatSerializer
from rest_framework import viewsets
from . import permissions


class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsInChat, )

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
