# Generated by Django 5.0.6 on 2024-05-16 10:46

import django.db.models.deletion
import traveler.helps
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Translator', 'Translator'), ('Manager', 'Manager'), ('Pilot', 'Pilot'), ('Accountant', 'Accountant'), ('Pioneer', 'Pioneer'), ('Other', 'Other')], default='Other', max_length=20)),
                ('image', models.ImageField(upload_to=traveler.helps.SaveMediafile.save_employe_image)),
                ('about_us', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
