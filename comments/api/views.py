from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    
    # Get all comments
    queryset = Comment.objects.all()
    
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    
    # Comments sorted in descending order
    ordering = ['-created_at']
    
    # Filter comments by post
    filterset_fields = ['post']