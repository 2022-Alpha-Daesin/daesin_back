from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from review.models import Review
from review.pagination import ReviewPageNumberPagination
from review.permissions import IsReviewAuthorOrReadOnly
from review.serializers import ReviewSerializer, ReviewListSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [IsReviewAuthorOrReadOnly]
    pagination_class = ReviewPageNumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['post__post_tags__tag__content']

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, images=self.request.FILES.getlist('images'),
                               tags=self.request.data.getlist('tags'), type="R")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user, images=self.request.FILES.getlist('images'),
                               tags=self.request.data.getlist('tags'))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
