from rest_framework.generics import RetrieveAPIView
from club.models import Club
from club.serializers import ClubSerializer


class ClubRetrieveAPIView(RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
