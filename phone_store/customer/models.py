from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    cart = models.ManyToManyField(Product, blank=True, related_name='customers')


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,
                             related_name='orders')
    products = models.ManyToManyField(Product)