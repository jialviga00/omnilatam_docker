from django.contrib import admin
from django.db import models
from .models import Payment, PaymentDetail

class PaymentDetailInline(admin.TabularInline):
    model = PaymentDetail
    extra = 3

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('__str__','customer', 'payment_date')
    list_filter = ['payment_date', 'customer']
    search_fields = ['payment_date', 'customer']
    inlines = [PaymentDetailInline]

admin.site.register(Payment, PaymentAdmin)
