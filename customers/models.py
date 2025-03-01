from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=3)
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=3)