from django.db import models

class sposor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    website = models.URLField()
    ty
    def __str__(self):
        return self.name
