from django.db import models

class sponsor(models.Model):
    
    def __str__(self):
        return self.name
