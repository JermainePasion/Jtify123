# Generated by Django 5.0.1 on 2024-03-19 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_artistregister_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistregister',
            name='user',
        ),
    ]
