# Generated by Django 4.1.3 on 2022-11-29 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='동아리 이름')),
                ('intro', models.CharField(max_length=1000, verbose_name='동아리 소개')),
                ('curriculum', models.CharField(max_length=1000, verbose_name='활동 내용')),
                ('signup_condition', models.CharField(max_length=500, verbose_name='가입 조건')),
                ('recruitment_period_start', models.DateTimeField(default=datetime.datetime.now, verbose_name='모집 시작 날짜')),
                ('recruitment_period_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='모집 종료 날짜')),
                ('representative_number', models.CharField(max_length=15, verbose_name='대표 전화번호')),
                ('place', models.CharField(max_length=20, null=True, verbose_name='동아리방 위치')),
                ('members_count', models.PositiveIntegerField(default=0, verbose_name='회원 수')),
                ('logo', models.ImageField(null=True, upload_to='club_logo', verbose_name='로고')),
                ('pamphlet', models.ImageField(null=True, upload_to='club_pamphlet', verbose_name='팜플렛')),
            ],
            options={
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clubs',
                'db_table': 'clubs',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Division',
                'verbose_name_plural': 'Division',
                'db_table': 'divisions',
            },
        ),
    ]
