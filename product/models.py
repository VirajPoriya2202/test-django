from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=25)

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=20)

