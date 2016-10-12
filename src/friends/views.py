from django.shortcuts import render
from .models import Relation, RelationSerializer
from rest_framework import viewsets


class RelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

# Create your views here.
