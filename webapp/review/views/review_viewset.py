from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from review.models import Review
from review.serializers.review_serializer import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, type="R")

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance.post)
        return Response(status=status.HTTP_204_NO_CONTENT)
