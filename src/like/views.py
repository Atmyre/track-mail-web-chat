from django.shortcuts import render
from .models import Like, LikeSerializer
from rest_framework import viewsets


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
# Create your views here.
