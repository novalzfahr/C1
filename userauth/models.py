from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
ROLES = [
    ('admin', 'ADMIN'),
    ('pelanggan', 'PELANGGAN')
]

class UserDataModel(AbstractUser):
    role = models.CharField(max_length=9, choices=ROLES, default='pelanggan')
    name = models.CharField(unique=True, max_length=100, blank=False, null=False, default='')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Your custom validation logic can be added here before saving
        if not self.name.strip() or self.name == '':
            raise ValueError("Name cannot be empty")

        # If validation passes, continue with the save operation
        super().save(*args, **kwargs)