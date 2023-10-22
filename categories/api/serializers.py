from rest_framework.serializers import ModelSerializer

from categories.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # Data to be serialized
        fields = ['id', 'title', 'slug', 'published', 'created']