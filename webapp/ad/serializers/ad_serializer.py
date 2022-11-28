from rest_framework.serializers import ModelSerializer
from post.models import Post,Image
from tag.models import PostTag,Tag
from ad.models import Advertisement
from post.serializers.post_serializer import PostSerializer


class ADSerializer(ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Advertisement
        fields = ['id', 'post', 'start_date', 'end_date', 'club']

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        images = validated_data.pop('images')
        tags = Tag.objects.filter(id__in=validated_data.pop('tags'))
        post = Post.objects.create(**post_data, type=validated_data.pop('type'), author=validated_data.pop('author'))
        advertisement = self.Meta.model._default_manager.create(post=post,
                                                                start_date=validated_data.pop('start_date'),
                                                                end_date=validated_data.pop('end_date'),
                                                                club=validated_data.get('club', None))
        for image in images:
            Image.objects.create(post=post,image=image)
        for tag in tags:
            PostTag.objects.create(post=post,tag=tag)
        return advertisement

    def update(self, instance, validated_data):
        post_data = validated_data.pop('post')
        post = instance.post
        post.title = post_data.get('title', post.title)
        post.content = post_data.get('content', post.content)
        post.save(update_fields=['title', 'content', 'updated_at'])
        instance.club = None
        instance = super().update(instance, validated_data)
        return instance