from rest_framework.serializers import ModelSerializer
from post.models import Post
from review.models import Review
from post.serializers import PostSerializer


class ReviewSerializer(ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Review
        fields = [
            'id',
            'post',
        ]

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        post = Post.objects.create(**post_data, type=validated_data.pop('type'), author=validated_data.pop('author'))
        review = self.Meta.model._default_manager.create(post=post)
        return review

    def update(self, instance, validated_data):
        post_data = validated_data.pop('post')
        post = instance.post
        post.title = post_data.get('title', post.title)
        post.content = post_data.get('content', post.content)
        post.save(update_fields=['title', 'content', 'updated_at'])
        return instance
