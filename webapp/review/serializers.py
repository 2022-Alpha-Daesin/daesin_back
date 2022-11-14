from rest_framework.serializers import ModelSerializer
from post.serializers import PostSerializer
from review.models import Review


class ReviewSerializer(ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'post',
        ]
