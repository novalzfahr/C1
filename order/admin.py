from django.contrib import admin

from .models import Promo, Item, Menu

# Register your models here.
admin.site.register(Promo)
admin.site.register(Item)
admin.site.register(Menu)