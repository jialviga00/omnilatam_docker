from django.contrib import admin
from .models import Shipment


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'shipment_date')
    list_filter = ['order', 'shipment_date']
    search_fields = ['order']


admin.site.register(Shipment, ShipmentAdmin)
