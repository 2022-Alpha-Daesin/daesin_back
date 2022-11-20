from rest_framework.serializers import ModelSerializer
from post.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']