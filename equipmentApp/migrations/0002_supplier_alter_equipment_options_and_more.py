# Generated by Django 4.2 on 2024-11-19 21:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(help_text="Enter the supplier's agency name (up to 50 characters).", max_length=50, verbose_name='Agency Name')),
                ('f_name', models.CharField(help_text="Enter the supplier's first name.", max_length=50, verbose_name='First Name')),
                ('l_name', models.CharField(help_text="Enter the supplier's last name.", max_length=50, verbose_name='Last Name')),
                ('phone_num', models.IntegerField(help_text='Enter an 8-digit phone number.', validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)], verbose_name='Phone Number')),
                ('address', models.CharField(help_text="Enter the supplier's address.", max_length=50, verbose_name='Address')),
                ('email', models.EmailField(help_text='Enter a valid email address.', max_length=254, verbose_name='Email Address')),
                ('sup_type', models.CharField(help_text='Enter the supplier type (e.g., equipment, service, etc.).', max_length=50, verbose_name='Supplier Type')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('is_active', models.BooleanField(default=True, help_text='Indicate if the supplier is currently active.', verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipment', 'verbose_name_plural': 'Equipment Items'},
        ),
        migrations.AddField(
            model_name='equipment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='The date and time when the equipment was last updated.', verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='brand',
            field=models.CharField(help_text='Enter the equipment brand.', max_length=50, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('like_new', 'Like New'), ('used', 'Used'), ('refurbished', 'Refurbished'), ('damaged', 'Damaged')], default='new', help_text='Select the equipment condition.', max_length=20, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a description for the equipment (optional).', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='eq_image',
            field=models.ImageField(blank=True, help_text='Upload an image of the equipment (optional).', null=True, upload_to='equipment_images/', verbose_name='Equipment Image'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(help_text='Enter the equipment name.', max_length=50, verbose_name='Equipment Name'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='stock_quantity',
            field=models.IntegerField(help_text='Enter the stock quantity (must be non-negative).', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stock Quantity'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='type',
            field=models.CharField(help_text='Enter the equipment type.', max_length=50, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='supplier',
            field=models.ForeignKey(help_text='Select the supplier for this equipment.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='equipmentApp.supplier', verbose_name='Supplier'),
        ),
    ]
