# Generated by Django 5.1.1 on 2024-09-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0005_alter_game_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.SlugField(max_length=200, primary_key=True, serialize=False),
        ),
    ]