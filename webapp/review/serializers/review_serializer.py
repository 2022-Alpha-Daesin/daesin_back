from rest_framework.serializers import ModelSerializer
from post.models import Post,Image
from review.models import Review
from tag.models import PostTag,Tag
from post.serializers import PostSerializer
from tag.serializers import PostTagSerializer
from post.serializers import ImageSerializer

class ReviewSerializer(ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Review
        fields = [
            'id',
            'post',
        ]

    def create(self, validated_data):
        images = validated_data.pop('images')
        tags = Tag.objects.filter(id__in=validated_data.pop('tags'))
        post_data = validated_data.pop('post')
        post = Post.objects.create(**post_data, type=validated_data.pop('type'), author=validated_data.pop('author'))
        for image in images:
            Image.objects.create(post=post,image=image)
        for tag in tags:
            PostTag.objects.create(post=post,tag=tag)
        review = self.Meta.model._default_manager.create(post=post)
        return review

    def update(self, instance, validated_data):
        post_data = validated_data.pop('post')
        post = instance.post
        post.title = post_data.get('title', post.title)
        post.content = post_data.get('content', post.content)
        post.save(update_fields=['title', 'content', 'updated_at'])
        return instance
