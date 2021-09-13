from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('identification','name', 'address', 'creation_date')
    list_filter = ['creation_date', 'identification', 'name']
    search_fields = ['identification', 'name']

admin.site.register(Customer, CustomerAdmin)

