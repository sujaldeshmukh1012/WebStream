# Generated by Django 3.0.7 on 2021-04-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_stream', '0002_auto_20210425_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/%d'),
        ),
    ]
