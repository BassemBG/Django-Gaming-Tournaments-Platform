from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Supplier(models.Model):
    agency_name = models.CharField(
        max_length=50, 
        verbose_name="Agency Name",
        help_text="Enter the supplier's agency name (up to 50 characters)."
    )
    f_name = models.CharField(
        max_length=50, 
        verbose_name="First Name", 
        help_text="Enter the supplier's first name."
    )
    l_name = models.CharField(
        max_length=50, 
        verbose_name="Last Name", 
        help_text="Enter the supplier's last name."
    )
    phone_num = models.IntegerField(
        validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],
        verbose_name="Phone Number",
        help_text="Enter an 8-digit phone number."
    )
    address = models.CharField(
        max_length=50, 
        verbose_name="Address", 
        help_text="Enter the supplier's address."
    )
    email = models.EmailField(
        max_length=254, 
        verbose_name="Email Address", 
        help_text="Enter a valid email address."
    )
    sup_type = models.CharField(
        max_length=50, 
        verbose_name="Supplier Type", 
        help_text="Enter the supplier type (e.g., equipment, service, etc.)."
    )
    created_date = models.DateField(
        auto_now_add=True, 
        verbose_name="Creation Date"
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Is Active", 
        help_text="Indicate if the supplier is currently active."
    )

    def __str__(self):
        return f"{self.agency_name} - {self.f_name} {self.l_name}"

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"


class Equipment(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name="Equipment Name", 
        help_text="Enter the equipment name."
    )
    type = models.CharField(
        max_length=50, 
        verbose_name="Type", 
        help_text="Enter the equipment type."
    )
    brand = models.CharField(
        max_length=50, 
        verbose_name="Brand", 
        help_text="Enter the equipment brand."
    )
    stock_quantity = models.IntegerField(
        validators=[MinValueValidator(0)], 
        verbose_name="Stock Quantity", 
        help_text="Enter the stock quantity (must be non-negative)."
    )
    eq_image = models.ImageField(
        upload_to='equipment_images/', 
        blank=True, 
        null=True, 
        verbose_name="Equipment Image", 
        help_text="Upload an image of the equipment (optional)."
    )
    condition = models.CharField(
        choices=[("new", "New"), ("like_new", "Like New"), ("used", "Used"), ("refurbished", "Refurbished"), ("damaged", "Damaged")], 
        max_length=20, 
        default="new", 
        verbose_name="Condition", 
        help_text="Select the equipment condition."
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Description", 
        help_text="Enter a description for the equipment (optional)."
    )
    supplier = models.ForeignKey(
        Supplier, 
        on_delete=models.CASCADE, 
        related_name="equipment", 
        verbose_name="Supplier", 
        help_text="Select the supplier for this equipment.",
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Last Updated", 
        help_text="The date and time when the equipment was last updated."
    )

    def __str__(self):
        return f"{self.name} - {self.type} - {self.brand}"

    def is_available(self):
        return self.stock_quantity > 0

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment Items"
