# Generated by Django 5.0.6 on 2024-07-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_tournament_tournamentparticipant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]
