from rest_framework import serializers

from tag.models import PostTag


class PostTagSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='tag.content', read_only=True)

    class Meta:
        model = PostTag
        fields = ['id', 'content', 'post', 'tag']
