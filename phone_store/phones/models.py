from django.db import models
from shop.models import Product


class Phone(models.Model):
    base_info = models.ForeignKey(Product, on_delete=models.CASCADE,
                                  related_name='add_info')
    memory = models.IntegerField()
    ddr = models.IntegerField()
    screen_size = models.DecimalField(max_digits=3, decimal_places=1)
    screen_width_px = models.IntegerField()
    screen_height_px = models.IntegerField()

    def __str__(self):
        return f'{self.base_info.brand} {self.base_info.name} {self.memory} GB'

