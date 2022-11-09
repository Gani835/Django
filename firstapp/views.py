from django.shortcuts import render,HttpResponse

# Create your views here.
def display(request):
    return render(request,'index.html')
    
