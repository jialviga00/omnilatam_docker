from django.db import models

class Shipment(models.Model):
	order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, null=True, blank=True)
	shipment_date = models.DateTimeField('Shipment date', auto_now_add=True)

	def __str__(self):
		return "Shipment-"+str(self.id).zfill(5)
