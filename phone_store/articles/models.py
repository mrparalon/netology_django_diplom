from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    phones = models.ManyToManyField(Phones, related_name='articles')