from django.db import models

from post.models import Post
from user.models import User


class Like(models.Model):
    class Meta:
        db_table = 'likes'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="좋아요 누르는 글",
        related_name="like",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="좋아요 누르는 유저",
    )
