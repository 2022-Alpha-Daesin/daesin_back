from django.db import models
from post.models import Post


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
        "club.Club",
        on_delete=models.CASCADE,
        related_name="club",
    )
