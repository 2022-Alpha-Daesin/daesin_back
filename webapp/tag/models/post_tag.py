from django.db import models

from post.models import Post
from .tag import Tag


class PostTag(models.Model):
    class Meta:
        db_table = 'post_tags'
        verbose_name = 'PostTag'
        verbose_name_plural = 'PostTags'

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_tags'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='post_tags'
    )
