from django.db import models


# Create your models here.
# https://docs.djangoproject.com/en/2.1/ref/models/fields/

class Product(models.Model):
    name = models.CharField(max_length=120) # max length of 120
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2) # 9999,99
    summary = models.TextField(default="Test")
