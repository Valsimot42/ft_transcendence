# Generated by Django 5.0.6 on 2024-08-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_rename_is_2fa_enabled_user_enable_2fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='totp_secret',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
