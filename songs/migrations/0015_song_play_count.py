# Generated by Django 4.2.8 on 2024-04-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0014_songplaycount'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='play_count',
            field=models.IntegerField(default=0),
        ),
    ]
