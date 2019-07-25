# Generated by Django 2.2.2 on 2019-07-24 18:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_slug'),
        ('customer', '0002_auto_20190724_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCustomerCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cart',
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='customers', through='customer.ProductCustomerCart', to='shop.Product'),
        ),
        migrations.AlterField(
            model_name='productcustomer',
            name='qty',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='productcustomercart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='productcustomercart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
