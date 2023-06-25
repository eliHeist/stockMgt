from django.db import models

from inventory.models import Product

# Create your models here.
class Order(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	vat = models.FloatField(max_length=100)
	discount = models.FloatField(max_length=100)
	payment_type = models.CharField(max_length=100)
	payment_status = models.BooleanField(default=True)

	def __str__(self):
		return self.date

	def getDate(self):
		return self.date
	
	def getTotalCost(self):
		total = 0
		for item in self.items.all():
			total += item.total()
		return "UGX {:,.0f}".format(total)


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	
	def total(self):
		return self.quantity * self.product.rate