# gamesman/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import re


def validate_file_size(value):
    
    pattern = r'^\d+(\.\d+)?\s*(B|KB|MB|GB|TB|PB|EB|ZB|YB)$'
    if not re.match(pattern, value, re.IGNORECASE):
        raise ValidationError("File size must be in the format of a number followed by a valid unit (e.g., '100MB', '1.5GB').")


class Game(models.Model):
    Game_Title = models.CharField(max_length=100, primary_key=True)
    Genre = models.CharField(max_length=50)
    Platform = models.CharField(max_length=50)
    Release_Date = models.DateField()
    Developer = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Nb_Players = models.IntegerField(validators=[MinValueValidator(1)])
    File_Size = models.CharField(max_length=20, validators=[validate_file_size])

    def __str__(self):
        return self.Game_Title

"""class SuggestedGame(models.Model):
    Game_Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50)
    Platform = models.CharField(max_length=50)
    Release_Date = models.DateField()
    Developer = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Nb_Players = models.IntegerField(validators=[MinValueValidator(1)])
    File_Size = models.CharField(max_length=20, validators=[validate_file_size])

    def __str__(self):
        return self.Game_Title"""
