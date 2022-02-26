from django.contrib import admin

from accounts import models
from .models import product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}



admin.site.register(product, ProductAdmin)
