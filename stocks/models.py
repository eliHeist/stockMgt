from django.db import models

from inventory.models import Product

# Create your models here.
class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField()
    time_registered = models.DateTimeField(auto_now_add=True)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Stock(models.Model):
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"Date: {self.date}"
    
    def getDate(self):
        return self.date