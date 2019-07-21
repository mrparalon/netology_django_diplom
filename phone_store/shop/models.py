from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    brand = models.CharField(max_length=128)
    picture = models.ImageField()
    reviews = models.ManyToManyField('Review', related_name='product', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.author} {self.score} звезд, {self.text[:10]} ...'
