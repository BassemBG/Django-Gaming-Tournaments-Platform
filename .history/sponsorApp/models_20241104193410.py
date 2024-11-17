from django.db import models
from django.core.validators import RegexValidator
class sponsor(models.Model):
    email_validator=RegexValidator( 
        regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        message='Please enter a valid email address'
    )
    name_validator=RegexValidator(
        regex='^[a-zA-Z]*$',
        message='Please enter a valid name'
    )
    address_validator=RegexValidator(
        regex='^[a-zA-Z0-9]*$',
        message='Please enter a valid address'
    )
    website_validator=RegexValidator(
        regex='^(http|https)://[a-zA-Z0-9]*$',
        message='Please enter a valid website'
    )
    email = models.EmailField(max_length=100, validators=[email_validator])
    name = models.CharField(max_length=100, validators=[name_validator])
    address = models.CharField(max_length=100, validators=[address_validator])
    website = models.URLField(max_length=100, validators=[website_validator])
    TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
