from tag.serializers import TagSerializer
from rest_framework.viewsets import ModelViewSet
from tag.models import Tag
from django_filters.rest_framework import DjangoFilterBackend


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['club_tags__club','post_tags__post','post_tags__post__type']