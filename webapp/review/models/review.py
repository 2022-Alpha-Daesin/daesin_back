from django.db import models
from post.models import Post


class Review(models.Model):
    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-post__updated_at']

    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name="review",
    )
