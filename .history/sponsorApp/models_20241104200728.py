from django.db import models


class sposor(models.Model):
    name_va
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    website = models.URLField()
    TYPE_CHOICES = [
        ('corporate', 'corporate'),
        ('small business', 'small business'),
        ('governmental', 'govermental'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
