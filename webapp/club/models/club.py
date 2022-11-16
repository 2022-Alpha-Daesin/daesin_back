from django.db import models
import datetime


class Club(models.Model):
    class Meta:
        db_table = 'clubs'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    division = models.ForeignKey(
        "club.Division",
        on_delete=models.CASCADE,
        verbose_name="구분"
    )
    name = models.CharField(
        max_length=20,
        null=False,
        verbose_name='동아리 이름'
    )
    intro = models.CharField(
        max_length=1000,
        null=False,
        verbose_name="동아리 소개"
    )
    curriculum = models.CharField(
        max_length=1000,
        verbose_name="활동 내용"
    )
    signup_condition = models.CharField(
        max_length=500,
        verbose_name="가입 조건",
    )
    recruitment_period_start = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name="모집 기간"
    )
    representative_number = models.CharField(
        max_length=15,
        verbose_name="대표 전화번호"
    )
    place = models.CharField(
        max_length=20,
        null=True,
        verbose_name="동아리방 위치",
    )
    members_count = models.PositiveIntegerField(
        default=0,
    )
    logo = models.ImageField(
        upload_to="club_logo",
    )
    pamphlet = models.ImageField(
        upload_to="club_pamphlet",
    )
