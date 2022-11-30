from rest_framework.generics import ListAPIView

from club.models import Club
from club.pagination import ClubPageNumberPagination
from club.serializers import ClubSerializer


class ClubListAPIView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    pagination_class = ClubPageNumberPagination
