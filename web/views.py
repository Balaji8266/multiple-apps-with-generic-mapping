from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def web(request):
    return render(request,'web.html')

def web1(request):
    return HttpResponse('<h1><marquee>JavaScript is used to provide dynamic functionality on web pages.</h1></marquee>')