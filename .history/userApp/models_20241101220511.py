from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

# Validators
def validate_username(value):
    if len(value) < 3:
        raise ValidationError('Username must be at least 3 characters long.')

def validate_first_name(value):
    if not value.isalpha():
        raise ValidationError('First name must contain only alphabetic characters.')

def validate_last_name(value):
    if not value.isalpha():
        raise ValidationError('Last name must contain only alphabetic characters.')

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('Password must contain at least one numeral.')
    if not any(char.isupper() for char in value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in value):
        raise ValidationError('Password must contain at least one special character.')

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
class Participant(AbstractBaseUser, PermissionsMixin):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, validators=[validate_username])
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, validators=[validate_first_name])
    last_name = models.CharField(max_length=30, validators=[validate_last_name])
    date_joined = models.DateTimeField(auto_now_add=True)
    token_activation = models.BooleanField(default=False)
    password = models.CharField(max_length=128, validators=[validate_password])
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('player', 'Player'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Add fields required for creating a superuser

    def save(self, *args, **kwargs):
        # Ensure password is hashed
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
