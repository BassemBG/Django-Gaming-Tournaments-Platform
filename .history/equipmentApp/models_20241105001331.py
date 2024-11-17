from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

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
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)], help_text="Enter the stock quantity (must be non-negative).")
    eq_image = models.ImageField(upload_to='equipment_images/', blank=True, null=True, verbose_name="Equipment's Image", help_text="Upload an image of the equipment (optional).")
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=20, default="new", help_text="Select the equipment condition.")
    description = models.TextField(blank=True, null=True, help_text="Enter a description for the equipment (optional).")
    def _str_(self):
        return f"{self.name} - {self.type} - {self.brand} - {self.model}"
    def is_available(self):
        return self.stock_quantity >= 0