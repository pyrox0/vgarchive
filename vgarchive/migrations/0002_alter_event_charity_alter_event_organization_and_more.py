# Generated by Django 5.1.1 on 2024-10-12 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vgarchive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='charity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vgarchive.charity', verbose_name='Supported Charity'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vgarchive.organization', verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='run',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vgarchive.event', verbose_name='Event'),
        ),
    ]
