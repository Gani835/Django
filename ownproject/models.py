from django.db import models

# Create your models here.

class ProductsDisplay(models.Model):
    ProdId=models.CharField(max_length=20)
    ProdImage=models.ImageField(upload_to='images/',blank=True,null=True)
    ProdName=models.CharField(max_length=20)
    ProdPrice=models.IntegerField()
    
    def __str__(self):
        return self.ProdName
    
# practicing the database concepts like insert,fetch,orm,etc

class Employee(models.Model):
    Employee_Id=models.IntegerField()
    Employee_Name=models.CharField(max_length=20)
    Employee_Address=models.CharField(max_length=20)
    Employee_Salary=models.IntegerField()
    
    