from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

class Supplier(models.Model):
    agency_name = models.CharField(max_length=50 , help_text="Enter the supplier's agency name (up to 50 characters).")
    f_name = models.CharField(max_length=50 , help_text="Enter the supplier's first name.")
    l_name = models.CharField(max_length=50 , help_text="Enter the supplier's last name.")
    phone_num = models.IntegerField(validators=[MinValueValidator(10000000) , MaxValueValidator(99999999)] )
    address = models.CharField(max_length=50 , help_text="Enter the supplier's address.")
    email = models.EmailField(max_length=254 , help_text="Enter a valid email address.")
    sup_type = models.CharField(max_length=50 , help_text="Enter the supplier type (e.g., equipment, service, etc.).")
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True,help_text="Indicate if the supplier is currently active.")
    def _str_(self):
        return f"{self.agency_name} - {self.f_name} {self.l_name}"


class Equipment(models.Model):
    DISP_EQ = [
        ("Disponible", "Disponible"),
        ("Not Disponible", "Not Disponible"),
    ]
    CONDITION_CHOICES = [
        ("new", "New"),
        ("like_new", "Like New"),
        ("used", "Used"),
        ("refurbished", "Refurbished"),
        ("damaged", "Damaged"), 
    ]
    name = models.CharField(max_length=50, help_text="Enter the equipment name.")
    type = models.CharField(max_length=50, help_text="Enter the equipment type.")
    brand = models.CharField(max_length=50, help_text="Enter the equipment brand.")
    model = models.CharField(max_length=50, help_text="Enter the equipment model.")
    price = models.FloatField(validators=[MinValueValidator(0)], help_text="Enter the price (must be non-negative).")
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)], help_text="Enter the stock quantity (must be non-negative).")
    disponibility = models.CharField(choices=DISP_EQ, max_length=20, default="Disponible", help_text="Select the availability status.")
    received_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='equipments', help_text="Select the supplier for this equipment.")
    eq_image = models.ImageField(upload_to='equipment_images/', blank=True, null=True, verbose_name="Equipment's Image", help_text="Upload an image of the equipment (optional).")
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=20, default="new", help_text="Select the equipment condition.")
    description = models.TextField(blank=True, null=True, help_text="Enter a description for the equipment (optional).")
    def _str_(self):
        return f"{self.name} - {self.type} - {self.brand} - {self.model}"
    def is_available(self):
        return self.stock_quantity>0
