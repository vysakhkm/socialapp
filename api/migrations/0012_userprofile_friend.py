# Generated by Django 4.1.4 on 2023-03-09 16:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_friend_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friend',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
