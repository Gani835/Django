from django.db import models

# Create your models here.


class Foodsales(models.Model):
    orderdate=models.DateField()
    region=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    product=models.CharField(max_length=20,null=True)
    quantity=models.IntegerField()
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)