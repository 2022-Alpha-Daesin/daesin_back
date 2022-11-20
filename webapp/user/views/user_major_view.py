from user.models import UserMajor
from user.serializers import UserMajorSerializer
from rest_framework.viewsets import ModelViewSet


class UserMajorViewSet(ModelViewSet):
    queryset = UserMajor.objects.all()
    serializer_class = UserMajorSerializer

    # usermajor추가하는거 admin에선 잘 되는데 postman에서는 잘 안됨
    # 형식의 문제인가..?
    # def perform_create(self, serializer): # 이슈 발생
    #     serializer.save(user_id=self.request.user.id)
