from django.shortcuts import render
from .models import Message, MessageSerializer
from rest_framework import viewsets
from rest_framework import permissions
#from .permissions import IsOwnerOrReadOnly


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
   # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        qs = super().get_queryset()
        chat_id = self.request.GET['chat_id']
        if chat_id:
            qs = qs.filter(chat_id=chat_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
