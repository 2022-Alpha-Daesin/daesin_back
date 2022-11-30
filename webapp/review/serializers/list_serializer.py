from rest_framework import serializers

from review.models import Review
from tag.serializers import PostTagSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    tags = PostTagSerializer(source='post.post_tags', many=True, read_only=True)
    author_name = serializers.CharField(source='post.author.nickname', read_only=True)
    title = serializers.CharField(source='post.title', read_only=True)
    content = serializers.CharField(source='post.content', read_only=True)
    updated_at = serializers.CharField(source='post.updated_at', read_only=True)
    created_at = serializers.CharField(source='post.created_at', read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'title',
            'content',
            'tags',
            'author_name',
            'comments_count',
            'created_at',
            'updated_at',
        ]

    def get_comments_count(self, review):
        return review.post.comment_set.count()
