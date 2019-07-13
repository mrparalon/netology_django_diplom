from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=128)
    memory = models.IntegerField()
    ddr = models.IntegerField()
    screen_size = models.FloatField()
    screen_width_px = models.IntegerField()
    screen_height_px = models.IntegerField()
    description = models.TextField()