from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    
    # Get posts that are published
    queryset = Post.objects.filter(published=True)
    
    # Search categories by "slug" instead of "id"
    lookup_field = 'slug'
    
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    
    # Posts sorted in descending order
    ordering = ['-created_at']
    
    # Filter category by slug
    filterset_fields = ['category__slug']
