# Generated by Django 5.1.1 on 2024-09-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_organization_table_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='bluesky',
            field=models.CharField(blank=True, max_length=200, verbose_name='Bluesky Account'),
        ),
    ]