from django.db import models

class sposor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    sponsor_type = models.CharField(max_length=50)
    sponsor_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor_date = models.DateField()
    sponsor_status = models.CharField(max_length=50)
    sponsor_notes = models.TextField()

    def __str__(self):
        return self.name
