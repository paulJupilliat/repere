
from django.db import models
from django.urls import reverse

from repere.settings import AUTH_USER_MODEL

# Create your models here.


class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    price = models.IntegerField(default=0)
    describtion = models.TextField(blank=True)
    first_image = models.ImageField(upload_to="products",blank= True, null=True)
    second_image = models.ImageField(upload_to="products", blank=True, null=True)
    third_image = models.ImageField(upload_to="products", blank=True, null=True)
    stock = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name


    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
class Order(models.Model):
    """
    Utilisateur -> lié à un compte
    Produit -> lié au produit
    Quantité -> interger
    Commandé ou non
    """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.product.product_name}({self.quantity}) pour {self.user.username}"
    
class Cart(models.Model):
    """
    Utilisateur -> lié à un compte
    Articles
    Commandé ou non
    Date de commande
    """
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.username
    
class Commande(models.Model):
    """
    1 ou plusieurs orders avec leur quantité
    le prix
    le client
    l'adresse de livraison
    """
    orders = models.ManyToManyField(Order)
    adresse = models.CharField(max_length=200)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    def total_price(self):
        return sum(order.product.price * order.quantity for order in self.orders.all())
    def __str__(self):
        
            
        return f" commande {self.orders.all()} pour {self.adresse} le {self.ordered_date} au prix de {self.total_price()} "
    