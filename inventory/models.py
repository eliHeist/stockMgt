from django.db import models

# Create your models here.
CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available")
)

class Brand(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=50, choices=CHOICES)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=50, choices=CHOICES)

	def __str__(self):
		return self.name

class Product(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	name = models.CharField(max_length=255)
	code = models.CharField(max_length=10)
	# image = models.ImageField(upload_to="media/product/images/")
	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	status = models.CharField(max_length=50, choices=CHOICES)

	def __str__(self):
		return f'{self.brand} {self.name}'
	
	def getCurrency(self):
		return "Shs. {:,.0f}".format(self.rate)