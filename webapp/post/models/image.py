from django.db import models
from post.models import Post


class Image(models.Model):
    """Model definition for Image."""

    class Meta:
        db_table = 'images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    image = models.ImageField(
        upload_to="post_image/",
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name= 'images',
        null=True,
        blank= True,
    )