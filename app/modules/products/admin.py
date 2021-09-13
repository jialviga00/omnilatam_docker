from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ['name', 'category']
    search_fields = ['name', 'category']

admin.site.register(Product, ProductAdmin)