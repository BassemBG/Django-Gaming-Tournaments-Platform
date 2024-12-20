# Generated by Django 4.2 on 2024-11-04 23:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the equipment name.', max_length=50)),
                ('type', models.CharField(help_text='Enter the equipment type.', max_length=50)),
                ('brand', models.CharField(help_text='Enter the equipment brand.', max_length=50)),
                ('stock_quantity', models.IntegerField(help_text='Enter the stock quantity (must be non-negative).', validators=[django.core.validators.MinValueValidator(0)])),
                ('eq_image', models.ImageField(blank=True, help_text='Upload an image of the equipment (optional).', null=True, upload_to='equipment_images/', verbose_name="Equipment's Image")),
                ('condition', models.CharField(choices=[('new', 'New'), ('like_new', 'Like New'), ('used', 'Used'), ('refurbished', 'Refurbished'), ('damaged', 'Damaged')], default='new', help_text='Select the equipment condition.', max_length=20)),
                ('description', models.TextField(blank=True, help_text='Enter a description for the equipment (optional).', null=True)),
            ],
        ),
    ]
