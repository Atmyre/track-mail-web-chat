from django.shortcuts import render
from .models import Chat, ChatSerializer
from rest_framework import viewsets


class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer