# Generated by Django 5.1.1 on 2024-09-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='category',
            field=models.CharField(default='Any%', max_length=200, verbose_name='Category'),
            preserve_default=False,
        ),
    ]