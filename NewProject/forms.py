from django import forms
from .models import JuicesInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    UserName=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=20)
    
    
class JuiceForm(forms.ModelForm):
    class Meta:
        model=JuicesInfo
        fields='__all__'
    
    
class CustUserCreate(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']