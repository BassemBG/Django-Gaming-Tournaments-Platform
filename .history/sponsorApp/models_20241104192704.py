from django.db import models

class sponsor(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    a
    def __str__(self):
        return self.name
