# Generated by Django 4.1.4 on 2023-03-11 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_userprofile_status_delete_friend_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='status',
            new_name='in_active',
        ),
    ]
