from django.db import models


class Major(models.Model):
    """Model definition for Major."""

    class Meta:
        db_table = 'majors'
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    COLLEGE_TYPE = (
        ('LIB', '글로벌인문지역대학'),  # college of Liberal Arts
        ('SOC', '사회과학대학'),  # college of Social Sciences
        ('LAW', '법과대학'),  # college of Law
        ('COM', '경상대학'),  # college of Commerce
        ('ENG', '창의공과대학'),  # college of Engineering
        ('DES', '조형대학'),  # college of design
        ('NAT', '과학기술대학'),  # college of Natural Science
        ('ART', '예술대학'),  # college of arts
        ('PHY', '체육대학'),  # college of Physical Education
        ('BUS', '경영대학'),  # college of business
        ('SOF', '소프트웨어융합대학'),  # college of software
        ('ARC', '건축대학'),  # college of architecture
        ('CAR', '자동차융합대학'),
        ('MOB', '미래모빌리티학과'),
    )

    college = models.CharField(
        max_length=3,
        choices=COLLEGE_TYPE,
        verbose_name='단과대',
    )
    department = models.CharField(
        max_length=40,
        null=True,
        verbose_name='학부'
    )
    sub_major = models.CharField(
        max_length=40,
        null=True,
        verbose_name='전공'
    )

    def get_full_major(self):
        if self.sub_major is not None:
            return f'{self.get_college_display()} {self.department} {self.sub_major}'
        return f'{self.get_college_display()} {self.department}'

    def __str__(self):
        if self.sub_major is None:
            return f"{self.department}"
        else:
            return f"{self.department} / {self.sub_major}"
