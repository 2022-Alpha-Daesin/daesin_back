from rest_framework.viewsets import ModelViewSet

from post.models import Image
from post.serializers.image_serializer import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
