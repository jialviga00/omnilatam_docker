from django.db import models

class Payment(models.Model):
	customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE, null=True, blank=True)
	payment_date = models.DateTimeField('Payment date', auto_now_add=True)
	amount = models.FloatField('Amount', blank=True, null=True)

	class Meta:
		ordering = ['payment_date']

	def __str__(self):
		return "Payment-"+str(self.id).zfill(5)


class PaymentDetail(models.Model):
	payment = models.ForeignKey("payments.Payment", on_delete=models.CASCADE, null=True, blank=True)
	order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, null=True, blank=True)
	amount = models.FloatField('Amount', blank=True, null=True)
	creation_date = models.DateTimeField('Creation date', auto_now_add=True)

	class Meta:
		ordering = ['creation_date']
	
	def __str__(self):
		return "PD-"+str(self.id).zfill(5)
