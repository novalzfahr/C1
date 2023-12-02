from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Feedback(models.Model):
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)