from django.db import models
from django.core.validators import RegexValidator

class sposor(models.Model):
    name_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    website = models.URLField()
    TYPE_CHOICES = [
        ('corporate', 'corporate'),
        ('small business', 'small business'),
        ('governmental', 'governmental'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
