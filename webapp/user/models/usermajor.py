from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserMajor(models.Model):
    """Model definition for UserMajor."""

    class Meta:
        db_table = 'usermajors'
        verbose_name = 'UserMajor'
        verbose_name_plural = 'UserMajors'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_majors',
        verbose_name='유저',
    )
    major = models.ForeignKey(
        'user.Major',
        on_delete=models.CASCADE,
        related_name='user_majors',
        verbose_name='학과'
    )
    number = models.IntegerField(
        default=1,
        verbose_name='전공순위'
    )
