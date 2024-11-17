from django.db import models
from django.core.validators import RegexValidator
class sponsor(models.Model):
    email_validator=RegexValidator( 
        regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        message='Please enter a valid email address'
    )
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    
    def __str__(self):
        return self.name
