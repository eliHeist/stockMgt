from django.contrib import admin

from inventory.models import Brand, Category, Product

# Register your models here.
admin.site.register(Category)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','status')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','quantity','code')