from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def python(request):
    return render(request, 'python.html')

def python1(request):
    return HttpResponse('Python')
