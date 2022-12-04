from rest_framework import serializers

from ad.models import Advertisement
from tag.serializers import PostTagSerializer


class AdvertisementListSerializer(serializers.ModelSerializer):
    tags = PostTagSerializer(source='post.post_tags', many=True, read_only=True)
    author_name = serializers.CharField(source='post.author.nickname', read_only=True)
    title = serializers.CharField(source='post.title', read_only=True)
    content = serializers.CharField(source='post.content', read_only=True)
    updated_at = serializers.DateTimeField(source='post.updated_at', read_only=True)
    created_at = serializers.DateTimeField(source='post.created_at', read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Advertisement
        fields = [
            'id',
            'title',
            'content',
            'tags',
            'author_name',
            'comments_count',
            'created_at',
            'updated_at',
            'start_date',
            'end_date',
        ]

    def get_comments_count(self, review):
        return review.post.comment_set.count()
