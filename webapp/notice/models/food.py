from django.db import models


class Food(models.Model):
    """Model definition for Food."""

    class Meta:
        db_table = 'food'
        verbose_name = 'Food'
        verbose_name_plural = 'Food'

    TIME_TYPE = (
        ('M', '아침'),
        ('A', '중식'),
        ('E', '석식'),
    )

    date = models.CharField(
        max_length=30,
        verbose_name='날짜'
    )
    restaurant = models.CharField(
        max_length=100,
        verbose_name='식당'
    )
    division = models.CharField(
        max_length=10,
        verbose_name='식당 이름'
    )
    time = models.CharField(
        max_length=1,
        choices=TIME_TYPE,
        verbose_name='시간'
    )
    menu = models.CharField(
        max_length=100,
        verbose_name='메뉴'
    )
