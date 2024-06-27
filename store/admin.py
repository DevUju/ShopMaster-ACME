from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stars')
    search_fields = ('name', 'description')
    ordering = ('-price',)

admin.site.register(Product, ProductAdmin)

