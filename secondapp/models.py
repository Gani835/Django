from django.db import models

# Create your models here.


class SignupPage(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    UserName=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    AgainPassword=models.CharField(max_length=20)

class LoginPage(models.Model):
    UserName=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    
    