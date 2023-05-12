from django.contrib import admin
from .models import Product

# Register your models here.
class ProductView(admin.ModelAdmin):
    list_display = ['id','name','rating']

admin.site.register(Product, ProductView)
