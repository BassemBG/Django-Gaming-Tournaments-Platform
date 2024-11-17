# In Participant/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class user(AbstractUser):
    cin_validator = RegexValidator(
        regex=r'^\d{8}$',
        message="This field must contain exactly 8 digits"
    )
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message="Invalid email format"
    )
    cin = models.CharField(primary_key=True, max_length=8, validators=[cin_validator])
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=255)
    USERNAME_FIELD = 'username'
    choices = (
        ('player', 'Player'),
        ('admin', 'Admin'),
    )
    role = models.CharField('role', choices=choices, max_length=255)    

    def clean(self):
        # Additional validation logic if needed
        pass
    class Meta:
        verbose_name_plural = 'users'

