from django.contrib import admin
from phones.models import Phone
from shop.models import Product


# class ProductInline(admin.StackedInline):
#     model = Phone

class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
