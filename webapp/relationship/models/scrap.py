from django.db import models
from post.models import Post
from user.models import User


class Scrap(models.Model):
    class Meta:
        db_table = 'scraps'
        verbose_name = 'Scrap'
        verbose_name_plural = 'Scraps'

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="스크랩 하는 글",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="스크랩 하는 유저",
    )
