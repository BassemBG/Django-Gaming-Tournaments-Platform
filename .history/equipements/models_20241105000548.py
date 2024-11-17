from django.db import models

class equipement(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    
    def __str__(self):
        return self.name
