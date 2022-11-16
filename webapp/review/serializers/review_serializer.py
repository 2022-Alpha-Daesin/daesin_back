from rest_framework.serializers import ModelSerializer
from post.serializers.post_serializer import PostSerializer
from review.models.review import Review


class ReviewSerializer(ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'post',
        ]
