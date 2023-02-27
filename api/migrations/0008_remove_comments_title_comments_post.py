# Generated by Django 4.1.4 on 2023-02-25 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_post_name_comments_title_remove_comments_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
    ]
