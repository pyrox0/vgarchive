# Generated by Django 5.1.1 on 2024-10-12 00:48

import django.db.models.deletion
import imagekit.models.fields
import vgarchive.models.charity
import vgarchive.models.event
import vgarchive.models.organization
import vgarchive.utils
import vgarchive.validators.bluesky
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Display Name')),
                ('short_name', models.CharField(blank=True, max_length=20, verbose_name='Short Name')),
                ('homepage', models.URLField(blank=True, verbose_name='Charity Homepage')),
                ('icon', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=vgarchive.models.charity._upload_icon, verbose_name='Icon/Favicon')),
                ('founded', models.IntegerField(default=2024, verbose_name='Founding Year')),
                ('twitter', models.CharField(blank=True, max_length=15, verbose_name='Twitter Account')),
                ('youtube', models.CharField(blank=True, max_length=200, verbose_name='Youtube Channel')),
                ('bluesky', models.CharField(blank=True, max_length=200, validators=[vgarchive.validators.bluesky.validate_bluesky], verbose_name='Bluesky Account')),
            ],
            options={
                'verbose_name_plural': 'Charities',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Game Name')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('homepage', models.URLField(blank=True, verbose_name='Organization Homepage')),
                ('icon', imagekit.models.fields.ProcessedImageField(upload_to=vgarchive.models.organization._upload_icon, verbose_name='Favicon/Icon')),
                ('banner', imagekit.models.fields.ProcessedImageField(upload_to=vgarchive.models.organization._upload_banner, verbose_name='Banner Image')),
                ('tracker', models.URLField(blank=True, verbose_name='Donation Tracker')),
                ('twitch', models.CharField(blank=True, max_length=25, verbose_name='Twitch Channel')),
                ('twitter', models.CharField(blank=True, max_length=15, verbose_name='Twitter Username')),
                ('youtube', models.CharField(blank=True, max_length=200, verbose_name='Youtube Channel')),
                ('bluesky', models.CharField(blank=True, max_length=200, validators=[vgarchive.validators.bluesky.validate_bluesky], verbose_name='Bluesky Account')),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('pronouns', models.CharField(blank=True, max_length=50, verbose_name='Pronouns')),
                ('twitch', models.CharField(blank=True, max_length=25, verbose_name='Twitch Channel')),
                ('youtube', models.CharField(blank=True, max_length=200, verbose_name='Youtube Channel')),
                ('twitter', models.CharField(blank=True, max_length=15, verbose_name='Twitter Username')),
                ('bluesky', models.CharField(blank=True, max_length=200, validators=[vgarchive.validators.bluesky.validate_bluesky], verbose_name='Bluesky Username')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Display Name')),
                ('short_name', models.CharField(blank=True, max_length=20, verbose_name='Short Name(optional)')),
                ('source', models.CharField(choices=[('tracker', 'GDQ Tracker'), ('oengus', 'Oengus'), ('manual', 'Manual Import')], default='manual', max_length=10, verbose_name='Event Source')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('homepage', models.URLField(blank=True, verbose_name='Event Homepage')),
                ('schedule', models.URLField(verbose_name='Schedule Link')),
                ('donation_total', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Donation Total')),
                ('donations', models.URLField(blank=True, verbose_name='Donations Page')),
                ('num_donations', models.IntegerField(verbose_name='Number of Donations')),
                ('youtube_playlist', models.URLField(blank=True, verbose_name='Youtube VOD Playlist')),
                ('banner', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=vgarchive.models.event._upload_banner, verbose_name='Banner Image')),
                ('charity', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='vgarchive.charity', verbose_name='Supported Charity')),
                ('organization', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='vgarchive.organization', verbose_name='Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.SlugField(max_length=200, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Category')),
                ('platform', models.CharField(max_length=200, verbose_name='Platform')),
                ('length', models.DurationField(verbose_name='Run Length')),
                ('youtube', models.URLField(validators=[vgarchive.utils.is_youtube_url], verbose_name='Youtube VOD Link')),
                ('twitch', models.URLField(blank=True, validators=[vgarchive.utils.is_twitch_url], verbose_name='Twitch VOD Link')),
                ('event', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='vgarchive.event', verbose_name='Event')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vgarchive.game', verbose_name='Game')),
                ('runners', models.ManyToManyField(to='vgarchive.runner', verbose_name='Runners')),
            ],
            options={
                'db_table_comment': 'Runs',
            },
        ),
    ]
