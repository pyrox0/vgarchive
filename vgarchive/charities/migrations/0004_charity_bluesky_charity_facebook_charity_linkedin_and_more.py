# Generated by Django 5.1.1 on 2024-09-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0003_alter_charity_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='bluesky',
            field=models.CharField(blank=True, max_length=200, verbose_name='Bluesky Account'),
        ),
        migrations.AddField(
            model_name='charity',
            name='facebook',
            field=models.CharField(blank=True, max_length=50, verbose_name='Facebook Page'),
        ),
        migrations.AddField(
            model_name='charity',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, verbose_name='Linkedin Account'),
        ),
        migrations.AddField(
            model_name='charity',
            name='twitter',
            field=models.CharField(blank=True, max_length=15, verbose_name='Twitter Account'),
        ),
        migrations.AddField(
            model_name='charity',
            name='youtube',
            field=models.CharField(blank=True, max_length=200, verbose_name='Youtube Channel'),
        ),
    ]