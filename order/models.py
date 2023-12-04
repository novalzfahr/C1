from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Promo(models.Model):
    ID_promo = models.CharField(max_length=200, primary_key=True)
    nama_promo = models.CharField(max_length=200, default="")
    deskripsi_promo = models.TextField(max_length=None)
    masa_berlaku = models.DateField()

class Item(models.Model):
    ID_item = models.CharField(max_length=200,primary_key=True, default= 0)
    user = models.CharField(max_length=200, default="")
    nama_item = models.CharField(max_length=200, default="")
    harga = models.FloatField(default=0)
    kuantitas = models.IntegerField(default=1)

class Menu(models.Model):
    ID_menu = models.CharField(max_length=200, primary_key=True)
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(max_length=None)
    harga = models.FloatField(default=0)
