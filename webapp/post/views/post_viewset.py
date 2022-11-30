from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.permissions import IsPostAuthorOrReadOnly
from post.serializers.post_serializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsPostAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly,
    ]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['type']

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
