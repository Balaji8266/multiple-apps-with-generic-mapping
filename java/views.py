from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#from django.http import HttpResponse

def java(request):
    return render(request, 'java.html')

def java1(request):
    return HttpResponse('<h1><marquee>Java Is a Compliled Programming Language.</h1></marquee>')
