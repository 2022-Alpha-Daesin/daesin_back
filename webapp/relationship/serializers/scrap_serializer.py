from rest_framework.serializers import ModelSerializer

from relationship.models import Scrap
from user.serializers import UserAbstractSerializer


class ScrapSerializer(ModelSerializer):
    user = UserAbstractSerializer(read_only=True)

    class Meta:
        model = Scrap
        fields = [
            'id',
            'post',
            'user',
        ]
        read_only_fields = [
            'user',
        ]
