# Generated by Django 5.1.3 on 2024-12-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
