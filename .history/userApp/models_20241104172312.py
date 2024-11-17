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
    string_validator = RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message="Invalid first name format"
    )

    cin = models.CharField(primary_key=True, max_length=8, validators=[cin_validator])
    email = models.EmailField(unique=True, max_length=255, validators=[email_validator])
    first_name = models.CharField(max_length=150, validators=[string_validator])
    last_name = models.CharField(max_length=150, validators=[string_validator])
    username = models.CharField(unique=True, max_length=255, validators=[string_validator])
    USERNAME_FIELD = 'username'
    role = models.CharField('role', choices=choices, max_length=255)    
    is_staff = models.BooleanField(default=False)
    def clean(self):
        # Additional validation logic if needed
        pass
    class Meta:
        verbose_name_plural = 'users'

