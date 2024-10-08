# Generated by Django 5.1.1 on 2024-09-20 20:29

import imagekit.models.fields
import vgarchive.charities.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0008_alter_charity_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=vgarchive.charities.models._upload_icon, verbose_name='Icon/Favicon'),
        ),
    ]
