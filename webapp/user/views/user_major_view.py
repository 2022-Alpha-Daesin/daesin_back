from user.models import UserMajor
from user.serializers import UserMajorSerializer
from rest_framework.viewsets import ModelViewSet


class UserMajorViewSet(ModelViewSet):
    queryset = UserMajor.objects.all()
    serializer_class = UserMajorSerializer

    def perform_create(self, serializer): 
        serializer.save(user= self.request.user)
