from django.shortcuts import render
from .models import Event, EventSerializer
from rest_framework import viewsets



class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Create your views here.
