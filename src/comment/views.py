from .models import Comment, CommentSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params.get('username'):
            qs = qs.filter(author__username=self.request.query_params.get('username'))
        return qs
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)