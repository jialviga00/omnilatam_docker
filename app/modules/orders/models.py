from django.db import models
from django import forms

class Order(models.Model):
    STATUS_OPTIONS = (
        ('PAID', 'PAID'),
        ('SENT', 'SENT'),
    )
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField('Order date', auto_now_add=True)
    status = models.CharField('Status', blank=True, null=True, choices=STATUS_OPTIONS, max_length=5)

    def __str__(self):
        return "Order-"+str(self.id).zfill(5)


class OrderDetail(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.FloatField("Amount")
    cant = models.FloatField("Cant")

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return "OD-"+str(self.id).zfill(5)
