# Generated by Django 5.0.6 on 2024-07-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_flag',
            field=models.BooleanField(default=False),
        ),
    ]
