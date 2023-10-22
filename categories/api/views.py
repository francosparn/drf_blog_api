from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.api.permissions import IsAdminOrReadOnly
from categories.api.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    
    # Get the categories that are published
    queryset = Category.objects.filter(published=True)
    
    # Search categories by "slug" instead of "id"
    lookup_field = 'slug'
    
    # Filter categories by title
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']