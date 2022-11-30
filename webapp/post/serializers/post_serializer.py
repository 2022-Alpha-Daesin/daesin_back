from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from post.models import Post
from tag.serializers import PostTagSerializer
from user.serializers import UserAbstractSerializer
from .image_serializer import ImageSerializer


class PostSerializer(ModelSerializer):
    author = UserAbstractSerializer(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)
    is_scraped = serializers.SerializerMethodField(read_only=True)
    image_list = ImageSerializer(source='images', many=True, read_only=True)
    tags = PostTagSerializer(source='post_tags', many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'image_list',
            'tags',
            'author',
            'type',
            'created_at',
            'updated_at',
            'like_count',
            'is_liked',
            'is_scraped',
        ]
        read_only_fields = ['type']
        extra_kwargs = {
            'title': {
                'error_messages': {
                    'required': '제목을 입력해주세요.',
                }
            },
            'content': {
                'error_messages': {
                    'required': '내용을 입력해주세요.',
                }
            }
        }

    def get_like_count(self, post):
        return post.like.count()

    def get_is_liked(self, post):
        try:
            user = self.get_request_user()
            return post.like.filter(user=user).exists()
        except:
            return False

    def get_is_scraped(self, post):
        try:
            user = self.get_request_user()
            return post.scrap.filter(user=user).exists()
        except:
            return False

    def get_request_user(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return user
