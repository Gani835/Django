from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import CreateUser,JuicesInfo
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,JuiceForm,CustUserCreate
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from.forms import CustUserCreate
# Create your views here.


def UserSignUpPage(request):
    context={'SignupForm':CustUserCreate}
    if request.method=='POST':
        newuser=CustUserCreate(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse('User Created Successfully. . . .')
        else:
            return redirect('usersignuppage')
        
    return render(request,'Signuppage.html',context)
    
    
def BacktoPage(request):
    return render(request,'backpage.html')
    
def UserLoginPage(request):
    context={}
    if request.method=='POST':
        usname=request.POST['uname']
        pswrd=request.POST['pwd']
        
        validuser=authenticate(UserName=usname,Password=pswrd)
        if validuser is not None:
            context={'loginform':LoginForm}
            if request.user.is_authenticated:
                return render(request,'mainpage.html',context)
            else:
                login(request,validuser)
                return render(request,'mainpage.html',context)
        else:
            return HttpResponse('you are an Invalid User please login with correct detailes.')
        
    return render(request,'userlogin.html')


def MainPage(request):
    
    # To view the form from frontend. . . .
    
    context={}
    context['juicesform']=JuiceForm()
    if request.method=='POST':
        data=JuiceForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request,'mainpage.html',context)
    
    # To render the detailes. . .
    
    #context={}
    #juices=JuicesInfo.objects.all()
    #context['juicesinfo']=juices
    #return render(request,'mainpage.html',context)
    
    # Paginatiion . . . .
    
    context={}
    juicesinfo=JuicesInfo.objects.all()
    page=Paginator(juicesinfo,4)
    pagenum=request.GET.get('page')
    p=page.get_page(pagenum)
    context['juicesinfo']=p
    
    return render(request,'mainpage.html',context)
   
def EcommercePage(request):
    return render(request,'1.html')

def SigningUpPage(request):
    return render(request,'signingup.html')

def dropdown(request):
    return render(request,'dropdown.html')


def Authentication(request):

    if request.method=='POST':
        uname=request.POST['usname']
        pswd=request.POST['passwrd']
        
        validuser=authenticate(username=uname,password=pswd)
        
        if validuser is not None:
            if request.user.is_authenticated:
                return render(request,'orminsert.html')
            else:
                login(request,validuser)    # for creating a session
                return render(request,'orminsert.html')
        else:
            return HttpResponse('Invalid User')
        
    return render(request,'uslogin.html')


def userlogout(request):
    logout(request)
    return render(request,'uslogin.html')


def UserSignUp(request):
    context={}
    obj=UserCreationForm()
    context['signupform']=obj
    
    if request.method=='POST':
        newuser=UserCreationForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse('u r signed up successfully. . ..')
        else:
            return redirect('signup')
    return render(request,'usersignup.html',context) 


# From ecommerce app. . . . 

def Authenticating(request):
    if request.method=='POST':
        usname=request.POST['uname']
        pswd=request.POST['pwd']
        
        validuser=authenticate(username=usname,password=pswd)
        if validuser is not None:
            if request.user.is_authenticated:
                return render(request,'2.html')
            else:
                login(request,validuser)
                return render(request,'2.html')
        else:
            return render(request,'backto.html')
        
    return render(request,'UserLoginPage.html')


def SignUpPage(request):
    context={'SignUpForm':CustUserCreate}
    
    if request.method=='POST':
        newuser=CustUserCreate(request.POST)
        if newuser.is_valid():
            newuser.save()
            return render(request,'success.html')
        else:
            return HttpResponse('Enter Correct Detailes. . .')
            
    return render(request,'usersignuppage.html',context)


def LogoutPage(request):
    logout(request)
    return render(request,'UserLoginPage.html')

