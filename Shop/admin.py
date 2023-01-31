from django.contrib import admin
from .models import *


# Register your models here.
class ItemProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price', 'P_price')


admin.site.register(userProfile)
admin.site.register(Category)
admin.site.register(Product, ItemProduct)
