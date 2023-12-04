from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

class Promotion(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    discount_amount = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Promotion for {self.menu.name}"
