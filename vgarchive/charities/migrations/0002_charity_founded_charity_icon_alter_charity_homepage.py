# Generated by Django 5.1 on 2024-08-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='founded',
            field=models.IntegerField(default=2024, verbose_name='Founding Year'),
        ),
        migrations.AddField(
            model_name='charity',
            name='icon',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Icon/Favicon'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='homepage',
            field=models.URLField(blank=True, verbose_name='Charity Homepage'),
        ),
    ]
