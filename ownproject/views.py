from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ProductsDisplay,Employee
from .forms import ProductInfo
from django.core.paginator import Paginator
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def ownproject(request):
    context={}
    context['prodinfo']=ProductInfo()
    if request.method=='POST':
        data=ProductInfo(request.POST)
        if data.is_valid():
            data.save()
        else:
            return HttpResponse('Data Not Saved')
        
    return render(request,'project.html',context)

def HomePage(request):
    context={}
    prodinfo=ProductsDisplay.objects.all()
    
    page=Paginator(prodinfo,2)
    pnum=request.GET.get('page')
    p=page.get_page(pnum)
    context['ProdInfo']=p
    return render(request,'phome.html',context)

# practicing the database concepts like insert,fetch,orm,etc

def fetchdata(request):
    context={}
    if request.method=='POST':
        eno=request.POST['empid']
        cur=connection.cursor()
        cur.execute('select * from employeeinfo where EmployeeId=%s',(eno,))
        data=cur.fetchall()
        print(data)
        context={'empinfo':data}
        return render(request,'fetchdata.html',context)
    return render(request,'fetchdata.html')

def insertdata(request):
    context={}
    if request.method=='POST':
        eid=request.POST['empid']
        ename=request.POST['empname']
        eage=request.POST['empage']
        eadd=request.POST['empaddress']
        esal=request.POST['empsalary']
        
        cur=connection.cursor()
        cur.execute('insert into employeeinfo values(%s,%s,%s,%s,%s)',(eid,ename,eage,eadd,esal,))
        data=cur.fetchall()
        context={'empinfo':data}
    return render(request,'insertdata.html',context)

@login_required(login_url='authent')
def orminsertdata(request):
    if request.method=='POST':
        eid=request.POST['empid']
        ename=request.POST['empname']
        eadd=request.POST['empaddress']
        esal=request.POST['empsalary']
        
        empinfo=Employee(Employee_Id=eid,Employee_Name=ename,Employee_Address=eadd,Employee_Salary=esal)
        empinfo.save()
        return HttpResponse('Data Saved Successfully. . . . ')
    return render(request,'orminsert.html')

def ormfetchdata(request):
    context={}
    data=Employee.objects.all()
    context={'fetchinfo':data}
    return render(request,'ormfetch.html',context)


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
            return render(request,'success.html')
        else:
            return redirect('signup')
    
    return render(request,'usersignup.html',context)
