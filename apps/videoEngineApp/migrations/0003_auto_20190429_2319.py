# Generated by Django 2.1.7 on 2019-04-29 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoEngineApp', '0002_auto_20190423_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='videofile',
        ),
        migrations.RemoveField(
            model_name='video',
            name='upload_date',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_views',
        ),
    ]
