# Generated by Django 4.1.2 on 2022-11-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.CharField(max_length=100, unique=True, verbose_name='태그'),
        ),
    ]