from rest_framework.serializers import ModelSerializer,CharField,SerializerMethodField

from relationship.models import Comment
from user.serializers import UserAbstractSerializer


class CommentSerializer(ModelSerializer):
    reply = SerializerMethodField()
    username = CharField(source='user.nickname',read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'username',
            'post',
            'content',
            'parent',
            'reply',
            'created_at',
            'updated_at',
        ]
 

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data
