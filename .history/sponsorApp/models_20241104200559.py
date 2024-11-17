from django.db import models

class sposor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    website = models.URLField()
    TYPE_CHOICES = [
        ('corporete', 'Gold'),
        ('small', 'Silver'),
        ('B', 'Bronze'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
