# Generated by Django 5.2 on 2025-04-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_youtube_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(default='O4MV5BRv-ps', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
