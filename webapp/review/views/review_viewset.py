from rest_framework.viewsets import ModelViewSet
from review.serializers.review_serializer import ReviewSerializer
from review.serializers.review_create_serializer import ReviewCreateSerializer
from review.models import Review
from post.models import Post


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()

    def get_queryset(self):
        if self.action != 'list':
            return Post.objects.all()
        print(self.action + "adfadsfdasfdasfadsfdasfdsaadfdfas")
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            print(self.action)
            return ReviewSerializer
        else:
            print(self.action)
            return ReviewCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, type="R")
