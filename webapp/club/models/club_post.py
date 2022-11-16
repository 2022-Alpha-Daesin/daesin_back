from django.db import models
from post.models import Post
from club.models import Club


class ClubPost(models.Model):
    class Meta:
        db_table = 'club_posts'
        verbose_name = 'ClubPost'
        verbose_name_plural = 'ClubPosts'

    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name="clubpost",
    )
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="club",
    )
