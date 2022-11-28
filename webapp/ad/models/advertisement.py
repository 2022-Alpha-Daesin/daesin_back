from django.db import models
from post.models import Post
from club.models import Club


class Advertisement(models.Model):
    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        ordering = ['-post__updated_at']

    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name='advertisement',
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    club = models.ForeignKey(
        Club,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='동아리명'
    )
