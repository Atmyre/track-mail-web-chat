from django.shortcuts import render
from .models import Like, LikeSerializer
from rest_framework import viewsets
from rest_framework import permissions


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
# Create your views here.
