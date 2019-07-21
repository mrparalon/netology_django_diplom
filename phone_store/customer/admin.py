from django.contrib import admin
from customer.models import Customer, Order


class CustomerAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)