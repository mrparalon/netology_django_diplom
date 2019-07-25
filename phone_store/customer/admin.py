from django.contrib import admin
from customer.models import Customer, Order


class ProductsInline(admin.StackedInline):
    model = Order.products.through
    fields = ['qty', 'product']


class CustomerOrderInline(admin.StackedInline):
    model = Order


class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerOrderInline]


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
