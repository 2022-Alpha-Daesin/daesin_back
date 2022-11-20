from rest_framework.viewsets import ModelViewSet
from post.serializers.image_serializer import ImageSerializer
from post.models import Image


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
