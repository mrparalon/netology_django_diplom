# Generated by Django 2.2.2 on 2019-07-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20190724_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cart',
            new_name='products_in_cart',
        ),
        migrations.AlterField(
            model_name='productcustomer',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='productcustomercart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='customer.Customer'),
        ),
    ]
