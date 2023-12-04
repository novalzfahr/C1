from django.db import models
from django.contrib.auth import get_user_model
from userauth.models import UserDataModel

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(UserDataModel, blank=False, null=False, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)