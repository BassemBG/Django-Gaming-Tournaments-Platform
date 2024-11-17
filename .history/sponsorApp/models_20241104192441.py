from django.db import models

class sponsor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
