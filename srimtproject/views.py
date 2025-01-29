from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"home.html")

def department(request):
    return render(request,"department.html")

def aboutSrimt(request):
    return render(request,"aboutSrimt.html")