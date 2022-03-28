from distlib import index
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sum=x+y
#     mul=x*y
#     div=x/y
#     return render(request,'result.html',{'resut':sum,'multi':mul,'divi':div})
