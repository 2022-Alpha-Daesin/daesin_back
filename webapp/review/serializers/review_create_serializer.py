from rest_framework.serializers import ModelSerializer
from post.models import Post
from review.models import Review
from post.serializers.post_serializer import PostSerializer


class ReviewCreateSerializer(ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        review = Review.objects.create(**validated_data)

        for posts in post_data:
            Post.objects.create(type="R", **posts)

        return review

    # class Meta:
    #     model = Post
    #     fields = [
    #         'id',
    #         'title',
    #         'content',
    #         'author',
    #         'type',
    #         'created_at',
    #         'updated_at'
    #     ]
    #     read_only_fields = [
    #         'type',
    #     ]
    #     extra_kwargs = {
    #         'title': {
    #             'error_messages': {
    #                 'required': '제목을 입력해주세요.',
    #             }
    #         },
    #         'content': {
    #             'error_messages': {
    #                 'required': '내용을 입력해주세요.',
    #             }
    #         }
    #     }
