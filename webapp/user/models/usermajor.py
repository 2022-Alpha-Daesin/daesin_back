from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class UserMajor(models.Model):
    """Model definition for UserMajor."""

    class Meta:
        db_table = 'usermajors'
        verbose_name = 'UserMajor'
        verbose_name_plural = 'UserMajors'

    major_user = models.ForeignKey(User, on_delete=models.CASCADE)
    major = models.ForeignKey('user.Major', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)