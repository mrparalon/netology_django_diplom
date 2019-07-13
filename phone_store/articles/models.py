from django.db import models
from phones.models import Phone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    phones = models.ManyToManyField(Phone, related_name='articles')
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name='articles')
    pub_date = models.DateTimeField(auto_now=True)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)