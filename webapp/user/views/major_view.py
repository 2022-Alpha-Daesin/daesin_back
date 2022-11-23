from user.models import Major
from user.serializers import MajorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class MajorViewSet(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

    filterset_fields = ['college']

    @action(detail=False,methods= ['GET'])
    def get_college_list(self,request):
        college_list = []
        for key,value in Major.COLLEGE_TYPE:
            college_list.append([key,value])
        return Response(college_list,status=status.HTTP_200_OK)

    