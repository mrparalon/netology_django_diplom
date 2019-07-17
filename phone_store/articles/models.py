from django.db import models
from phones.models import Phone
from django.contrib.auth.models import User
from pytils.translit import slugify


class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    phones = models.ManyToManyField(Phone, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
