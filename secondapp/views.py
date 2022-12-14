from django.shortcuts import render,redirect
from django.http import HttpResponse
#from . models import SignupPage,LoginPage
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Signup Page Creation. . . . 

def usersignup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user )
            return redirect('login')
    context={'form':form}
    return render(request,'signup.html',context)

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or Password is incorrect')
            
    context={}
    return render(request,'login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def homepage(request):
    return render(request,'home.html')