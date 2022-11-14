from rest_framework.generics import ListAPIView
from review.models.review import Review
from review.serializers.review_serializer import ReviewSerializer


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
