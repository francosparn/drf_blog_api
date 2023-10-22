from rest_framework import serializers

from comments.models import Comment

from posts.api.serializers import PostSerializer
from users.api.serializers import UserInfoSerializer


class CommentSerializer(serializers.ModelSerializer):
    # Serialize the "user" and "post" field to a string
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        # Data to be serialized
        fields = ['id', 'content', 'created_at', 'user', 'post']