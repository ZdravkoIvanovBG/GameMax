# Generated by Django 5.1.3 on 2024-12-01 18:42

import GameMax.app_users.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('franchise_image', models.ImageField(upload_to='franchise_images/', validators=[GameMax.app_users.validators.MaxFileSizeValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'The Title Is At Least 5 Chaacters Long!')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('welcome_message', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('game_image', models.ImageField(upload_to='game_images/')),
                ('pegi', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                ('game_abbreviation', models.CharField(max_length=15)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Survival', 'Survival'), ('Strategy', 'Strategy'), ('Adventure', 'Adventure'), ('First Person', 'First Person'), ('MMO', 'MMO'), ('Sports', 'Sports'), ('Open World', 'Open World')], max_length=20)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.franchise')),
            ],
        ),
    ]
