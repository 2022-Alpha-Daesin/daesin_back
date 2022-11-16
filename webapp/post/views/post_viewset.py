from rest_framework.viewsets import ModelViewSet
from post.serializers.post_serializer import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from post.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['type']

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
