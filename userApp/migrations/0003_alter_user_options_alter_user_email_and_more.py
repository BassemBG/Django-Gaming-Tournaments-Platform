# Generated by Django 4.2 on 2024-11-04 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_user_options_user_groups_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid email format', regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Invalid first name format', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Invalid first name format', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('sponsor', 'Sponsor'), ('player', 'Player')], max_length=255, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid first name format', regex='^[a-zA-Z]+$')]),
        ),
    ]
