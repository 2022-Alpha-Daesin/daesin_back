# Generated by Django 4.1.3 on 2022-11-29 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-post__updated_at'], 'verbose_name': 'Advertisement', 'verbose_name_plural': 'Advertisements'},
        ),
    ]