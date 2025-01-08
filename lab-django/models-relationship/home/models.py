from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    orders = models.ManyToManyField('Order', through='OrderDetail')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderDetail')

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
