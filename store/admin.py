from django.contrib import admin
from store.models import Products, Order, Cart, Commande


# Register your models here.
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Commande)