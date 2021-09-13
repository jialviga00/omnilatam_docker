from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import Group
from .models import Order, OrderDetail
from django.contrib import admin

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__','customer', 'status', 'order_date')
    list_filter = ['order_date', 'status', 'customer']
    search_fields = ['order_date', 'status', 'customer']
    inlines = [OrderDetailInline]

admin.site.register(Order, OrderAdmin)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)