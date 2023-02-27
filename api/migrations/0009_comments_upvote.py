# Generated by Django 4.1.4 on 2023-02-27 02:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_remove_comments_title_comments_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='upvote',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
