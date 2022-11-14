from rest_framework.generics import RetrieveAPIView
from review.models import Review
from review.serializers import ReviewSerializer


class ReviewRetrieveAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
