# Generated by Django 4.2.6 on 2024-10-21 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0035_nbafinalspredictionquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nbafinalspredictionquestion',
            name='east_team',
        ),
        migrations.RemoveField(
            model_name='nbafinalspredictionquestion',
            name='predicted_losses',
        ),
        migrations.RemoveField(
            model_name='nbafinalspredictionquestion',
            name='predicted_winner',
        ),
        migrations.RemoveField(
            model_name='nbafinalspredictionquestion',
            name='predicted_wins',
        ),
        migrations.RemoveField(
            model_name='nbafinalspredictionquestion',
            name='west_team',
        ),
    ]