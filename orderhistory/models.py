from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields for items as needed

# class DataPembayaran(models.Model):
    # Define fields for payment data
    # ...

class Pelanggan(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields for customer details as needed

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_harga = models.FloatField()
    promo_used = models.BooleanField(default=False)
    # data_pembayaran = models.OneToOneField(DataPembayaran, on_delete=models.CASCADE)
    status_order = models.CharField(max_length=50)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.pk} - {self.pelanggan.name}"
