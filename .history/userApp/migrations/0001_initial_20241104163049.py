# Generated by Django 4.2 on 2024-11-04 15:11

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cin', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='This field must contain exactly 8 digits', regex='^\\d{8}$')])),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('role', models.CharField(choices=[('Player', 'Player'), ('Admin', 'Admin')], max_length=255, verbose_name='participant_category')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='participant_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='participant_set', to='auth.permission')),
            ],
            options={
                'verbose_name_plural': 'Participants',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
