from django.contrib import admin
from .models import Store, Category, Product, Order, OrderDetail

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
