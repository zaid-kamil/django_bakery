from django.contrib import admin
from .models import Collection, Product, ProductImage


admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(ProductImage)