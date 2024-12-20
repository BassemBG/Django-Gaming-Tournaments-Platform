# Generated by Django 4.2 on 2024-11-25 20:53

import SponsorshipApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SponsorshipApp', '0002_alter_sponsorship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='start_date',
            field=models.DateField(validators=[SponsorshipApp.models.start_date_validator]),
        ),
    ]
