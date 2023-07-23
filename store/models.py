from django.db import models

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
