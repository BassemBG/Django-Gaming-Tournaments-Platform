from django.db import models

class sponsor(models.Model):
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
