# Generated by Django 5.1.3 on 2024-12-01 14:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
