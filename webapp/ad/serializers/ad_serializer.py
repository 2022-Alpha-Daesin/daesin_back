from rest_framework.serializers import ModelSerializer
from post.models import Post
from ad.models import Advertisement
from post.serializers.post_serializer import PostSerializer


class ADSerializer(ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Advertisement
        fields = ['id', 'post', 'start_date', 'end_date']

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        post = Post.objects.create(**post_data, type=validated_data.pop('type'), author=validated_data.pop('author'))
        advertisement = self.Meta.model._default_manager.create(post=post, start_date=validated_data.pop('start_date'), end_date=validated_data.pop('end_date'))
        return advertisement

    def update(self, instance, validated_data):
        # start_date, end_date 어떻게...?
        post_data = validated_data.pop('post')
        post = instance.post
        post.title = post_data.get('title', post.title)
        post.content = post_data.get('content', post.content)
        post.save(update_fields=['title', 'content', 'updated_at'])
        instance = super().update(instance, validated_data)
        return instance