# Generated by Django 5.1.1 on 2024-10-02 16:47

import vgarchive.validators.bluesky
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0008_alter_runner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='bluesky',
            field=models.CharField(blank=True, max_length=200, validators=[vgarchive.validators.bluesky.validate_bluesky], verbose_name='Bluesky Username'),
        ),
    ]