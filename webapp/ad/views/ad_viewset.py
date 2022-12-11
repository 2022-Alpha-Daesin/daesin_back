from datetime import datetime, timedelta

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ad.models import Advertisement
from ad.pagination import AdPageNumberPagination
from ad.permissions import IsAdAuthorOrReadOnly
from ad.serializers import ADSerializer, AdvertisementListSerializer


class ADViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    permission_classes = [
        IsAdAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly,
    ]
    # pagination_class = AdPageNumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['post__post_tags__tag__content']
    ordering = ['-post.updated_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertisementListSerializer
        return ADSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, images=self.request.FILES.getlist('images'),
                               tags=self.request.data.getlist('tags'), type="A")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user, images=self.request.FILES.getlist('images'),
                               tags=self.request.data.getlist('tags'))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 당일 마감 홍보글 (마감 시간이 지난 홍보글은 제외)
    @action(detail=False, methods=['GET'])
    def deadline_0(self, request):
        # paginator = PageNumberPagination()
        # paginator.page_size = 4
        day = datetime.today() - timedelta(days=0)
        ads = Advertisement.objects.filter(Q(end_date__date=day) & Q(end_date__gt=datetime.now()))
        # result = paginator.paginate_queryset(ads, request)
        serializer = self.get_serializer(ads, many=True)
        # response = paginator.get_paginated_response(serializer.data)
        response = Response(serializer.data)
        return response

    # 마감 1일 전 홍보글
    @action(detail=False, methods=['GET'])
    def deadline_1(self, request):
        response = self.get_deadline_ad(request, 1)
        return response

    # 마감 2일전 홍보글
    @action(detail=False, methods=['GET'])
    def deadline_2(self, request):
        response = self.get_deadline_ad(request, 2)
        return response

    # 마감 3일전 홍보글
    @action(detail=False, methods=['GET'])
    def deadline_3(self, request):
        response = self.get_deadline_ad(request, 3)
        return response

    def get_deadline_ad(self, request, deadline_date):
        # paginator = PageNumberPagination()
        # paginator.page_size = 4
        day = datetime.today() + timedelta(days=deadline_date)
        ads = Advertisement.objects.filter(end_date__date=day)
        # result = paginator.paginate_queryset(ads, request)
        serializer = self.get_serializer(ads, many=True)
        # response = paginator.get_paginated_response(serializer.data)
        response = Response(serializer.data)
        return response
