from django.db import models
from userauth.models import UserDataModel

# class DataPembayaran(models.Model):
    # Define fields for payment data
    # ...\

class FinishedOrder(models.Model):
    # items = models.ManyToManyField(Item)
    total_harga = models.FloatField()
    promo_used = models.BooleanField(default=False)
    # data_pembayaran = models.OneToOneField(DataPembayaran, on_delete=models.CASCADE)
    status_order = models.CharField(max_length=50)
    user = models.ForeignKey(UserDataModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.pk} - {self.pelanggan.name}"
