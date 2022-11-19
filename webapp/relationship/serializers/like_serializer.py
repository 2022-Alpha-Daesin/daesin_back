from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from relationship.models import Like
from user.serializers import UserAbstractSerializer


class LikeSerializer(ModelSerializer):
    user = UserAbstractSerializer(read_only=True)

    class Meta:
        model = Like
        fields = [
            'id',
            'post',
            'user',
        ]
        read_only_fields = [
            'user',
        ]
