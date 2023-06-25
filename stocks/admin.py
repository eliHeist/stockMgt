from django.contrib import admin

from stocks.models import Batch, Stock

# Register your models here.
admin.site.register(Batch)
admin.site.register(Stock)