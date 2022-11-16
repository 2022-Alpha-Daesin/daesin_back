from django.db import models
from post.models import Post


class Image(models.Model):
    """Model definition for Image."""

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    image = models.ImageField(
        upload_to="post_image",
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )