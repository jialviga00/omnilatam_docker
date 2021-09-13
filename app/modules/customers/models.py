from django.db import models

class Customer(models.Model):
    identification = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return str(self.name)
