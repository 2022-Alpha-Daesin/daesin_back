import datetime

from django.db import models


class Club(models.Model):
    class Meta:
        db_table = 'clubs'
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    division = models.ForeignKey(
        "club.Division",
        on_delete=models.CASCADE,
        verbose_name="구분",
        null=True,
    )
    name = models.CharField(
        max_length=20,
        null=False,
        verbose_name='동아리 이름',
    )
    intro = models.CharField(
        max_length=1000,
        null=False,
        verbose_name="동아리 소개",
    )
    curriculum = models.CharField(
        max_length=1000,
        verbose_name="활동 내용",
    )
    signup_condition = models.CharField(
        max_length=500,
        verbose_name="가입 조건",
    )
    recruitment_period_start = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name="모집 시작 날짜",
    )
    recruitment_period_end = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name="모집 종료 날짜",
    )
    representative_number = models.CharField(
        max_length=15,
        verbose_name="대표 전화번호",
    )
    place = models.CharField(
        max_length=20,
        null=True,
        verbose_name="동아리방 위치",
    )
    members_count = models.PositiveIntegerField(
        default=0,
        verbose_name="회원 수",
    )
    # TODO logo 와 pamphlet 은 default image 지정 필요 할 듯
    logo = models.ImageField(
        upload_to="club_logo",
        verbose_name="로고",
        null=True,
    )
    pamphlet = models.ImageField(
        upload_to="club_pamphlet",
        verbose_name="팜플렛",
        null=True,
    )
