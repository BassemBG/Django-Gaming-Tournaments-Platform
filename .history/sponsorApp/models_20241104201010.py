from django.db import models
from django.core.validators import RegexValidator

class sposor(models.Model):
    name_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    email_validator = RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'Invalid email format.')
    address_validator = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only letters and numbers are allowed.')
    website_validator = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only letters and numbers are allowed.')
    name = models.CharField(max_length=100, validators=[name_validator])
    email = models.EmailField(validators=[email_validator])
    address = models.CharField(max_length=100, validators=[address_validator])
    website = models.URLField()
    TYPE_CHOICES = [
        ('corporate', 'corporate'),
        ('small business', 'small business'),
        ('governmental', 'governmental'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
