from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from post.models import Post
from post.permissions import IsPostAuthorOrReadOnly
from post.serializers.post_serializer import PostSerializer
from relationship.models import Scrap


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsPostAuthorOrReadOnly,
    ]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['type']

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    # 내가 쓴 글
    @action(detail=False, methods=['GET'])
    def my_post(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 6
        posts = Post.objects.filter(author=self.request.user)
        results = paginator.paginate_queryset(posts, request)
        serializer = self.get_serializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    # 스크랩한 글
    @action(detail=False, methods=['GET'])
    def scrap_post(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 6
        scraps = Scrap.objects.filter(user=self.request.user)
        posts = [scrap.post for scrap in scraps]
        results = paginator.paginate_queryset(posts, request)
        serializer = self.get_serializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)
