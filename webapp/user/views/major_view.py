from user.models import Major
from user.serializers import MajorSerializer
from rest_framework.viewsets import ModelViewSet


class MajorViewSet(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
