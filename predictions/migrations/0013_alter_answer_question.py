# Generated by Django 4.2.6 on 2024-04-03 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0012_answer_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(limit_choices_to=models.Q(('season_id', models.F('season_id'))), on_delete=django.db.models.deletion.CASCADE, to='predictions.question'),
        ),
    ]
