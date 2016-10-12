from django.shortcuts import render
from .models import Community, CommunitySerializer
from rest_framework import viewsets


class CommunityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Create your views here.
