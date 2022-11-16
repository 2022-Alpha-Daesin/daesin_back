from django.db import models
from user.models.major import Major


class Division(models.Model):
    class Meta:
        db_table = 'divisions'
        verbose_name = 'Division'
        verbose_name_plural = 'Division'

    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
    )
