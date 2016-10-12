from django.shortcuts import render
from .models import Message, MessageSerializer
from rest_framework import viewsets


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
# Create your views here.
