from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from relationship.models import Comment
from relationship.paginatiion import CommentPageNumberPagination
from relationship.permissions import IsAuthorOrReadOnly
from relationship.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPageNumberPagination
    permission_classes = [
        IsAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)
