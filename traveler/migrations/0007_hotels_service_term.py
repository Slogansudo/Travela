# Generated by Django 5.0.6 on 2024-05-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0006_alter_aboutus_options_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='service_term',
            field=models.IntegerField(default=1),
        ),
    ]