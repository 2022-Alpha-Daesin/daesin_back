from django.db import models
from club.models import Club
from tag.models import Tag


class ClubTag(models.Model):
    class Meta:
        db_table = 'club_tags'
        verbose_name = 'ClubTag'
        verbose_name_plural = 'ClubTags'

    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )

