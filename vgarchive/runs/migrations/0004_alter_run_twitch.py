# Generated by Django 5.1.1 on 2024-09-14 20:02

import vgarchive.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0003_game_runner_remove_run_runners_alter_run_twitch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='twitch',
            field=models.URLField(blank=True, validators=[vgarchive.utils.is_twitch_url], verbose_name='Twitch VOD Link'),
        ),
    ]
