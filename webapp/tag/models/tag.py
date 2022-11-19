from django.db import models


class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    content = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
