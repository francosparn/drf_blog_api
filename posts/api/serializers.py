from rest_framework.serializers import ModelSerializer

from posts.models import Post
from users.api.serializers import UserInfoSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(ModelSerializer):
    # Get the serialized fields of the User and Category models
    user = UserInfoSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Post
        # Data to be serialized
        fields = ['id', 'title', 'content', 'slug', 'image', 'created_at', 'published', 'user', 'category']