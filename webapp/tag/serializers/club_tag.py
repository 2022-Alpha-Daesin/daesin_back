from rest_framework.serializers import ModelSerializer
from tag.models import ClubTag


class ClubTagSerializer(ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'