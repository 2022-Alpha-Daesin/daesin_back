from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from relationship.models import Comment
from user.serializers import UserAbstractSerializer


class CommentSerializer(ModelSerializer):
    reply = SerializerMethodField()
    user = UserAbstractSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'content',
            'parent',
            'reply',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'user',
        ]

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data
