from rest_framework.serializers import ModelSerializer
from post.models import Post
from user.serializers import UserAbstractSerializer


class PostSerializer(ModelSerializer):
    author = UserAbstractSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author',
            'type',
            'created_at',
            'updated_at'
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
