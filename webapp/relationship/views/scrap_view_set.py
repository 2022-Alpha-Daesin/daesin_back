from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from relationship.models import Scrap
from relationship.paginatiion import ScrapPageNumberPagination
from relationship.serializers import ScrapSerializer


class ScrapViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Scrap.objects.all()
    serializer_class = ScrapSerializer
    pagination_class = ScrapPageNumberPagination
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if Scrap.objects.filter(Q(user=self.request.user) & Q(post=self.request.POST['post'])).exists():
            return Response(
                {
                    'error': '사용자가 이미 스크랩을 하였습니다.'
                }
            )
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
