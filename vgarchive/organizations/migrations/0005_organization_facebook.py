# Generated by Django 5.1.1 on 2024-09-14 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_organization_bluesky'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='facebook',
            field=models.CharField(blank=True, max_length=50, verbose_name='Facebook Page'),
        ),
    ]
