from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('canceled', 'Canceled'),
    ]

    items = models.TextField()  # Assuming a simple representation of items as text
    total_harga = models.FloatField()
    promo_used = models.BooleanField(default=False)
    status_order = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    pelanggan_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Order {self.pk} - {self.pelanggan_name}"
