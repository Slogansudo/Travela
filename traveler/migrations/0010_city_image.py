# Generated by Django 5.0.6 on 2024-05-16 18:05

import traveler.helps
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0009_remove_team_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(default=1, upload_to=traveler.helps.SaveMediafile.save_city_media),
            preserve_default=False,
        ),
    ]