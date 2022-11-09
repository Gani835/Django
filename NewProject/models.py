from django.db import models

# Create your models here.

class CreateUser(models.Model):
    FirstName=models.CharField(max_length=20,null=True)
    LastName=models.CharField(max_length=50)
    EmailAddress=models.CharField(max_length=50)
    UserName=models.CharField(max_length=20,null=True)
    Password=models.CharField(max_length=20)
    ConfirmPassword=models.CharField(max_length=20)


class JuicesInfo(models.Model):
    JuiceId=models.CharField(max_length=20)
    JuiceImage=models.ImageField(upload_to='images/',null=True,blank=True)
    JuiceName=models.CharField(max_length=20)
    JuicePrice=models.IntegerField(null=True)
    
    def __str__(self):
        return self.JuiceName


