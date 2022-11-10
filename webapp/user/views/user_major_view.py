from user.models import UserMajor
from user.serializers import UserMajorSerializer
from rest_framework.viewsets import ModelViewSet


class UserMajorViewSet(ModelViewSet):
    queryset = UserMajor.objects.all()
    serializer_class = UserMajorSerializer
