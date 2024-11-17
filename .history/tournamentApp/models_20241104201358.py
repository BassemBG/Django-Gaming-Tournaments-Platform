from django.db import models

class tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('upcoming', 'Upcoming'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ]
    )
    prize = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    location = models.CharField(max_length=100)
    website = models.URLField()
    TYPE_CHOICES = [
        ('corporate', 'corporate'),
        ('small business', 'small business'),
        ('governmental', 'governmental'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name