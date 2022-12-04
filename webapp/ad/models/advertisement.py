from django.db import models

from club.models import Club
from post.models import Post


class Advertisement(models.Model):
    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        ordering = ['end_date']  # 바꾸면 안 됩니다! 마감 홍보글 호출에 변동이 생길 수 있습니다.

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
