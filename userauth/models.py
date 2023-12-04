from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
ROLES = [
    ('admin', 'ADMIN'),
    ('pelanggan', 'PELANGGAN')
]

class UserDataModel(AbstractUser):
    role = models.CharField(max_length=9, choices=ROLES, default='pelanggan')
    name = models.CharField(max_length=100, default='NewUser')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
