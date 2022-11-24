from django.db import models


class Notice(models.Model):
    """Model definition for Notice."""

    class Meta:
        db_table = 'notices'
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    major = models.CharField(
        max_length=30,
    )
    title = models.CharField(
        max_length=100,
    )
    url = models.CharField(
        max_length=100,
    )
