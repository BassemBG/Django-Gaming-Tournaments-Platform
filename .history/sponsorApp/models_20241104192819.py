from django.db import models

class sponsor(models.Model):
    email_validator=    Re
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
