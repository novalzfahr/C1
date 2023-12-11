from django.contrib import admin

# Register your models here.
from .models import UserDataModel

admin.site.register(UserDataModel)