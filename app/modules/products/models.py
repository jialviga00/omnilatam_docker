from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=50)
	category = models.CharField(max_length=20)
	description = models.CharField(max_length=200, null=True, blank=False)

	def __str__(self):
		return str(self.name)