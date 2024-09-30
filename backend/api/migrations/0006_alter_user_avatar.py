# Generated by Django 5.0.5 on 2024-06-15 12:35

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_avatar_user_chat_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', validators=[api.models.validate_file_size]),
        ),
    ]
