"""
URL configuration for project7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from python.views import *
from java.views import *
from web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('python/', python, name='python'),
    path('python1/', python1, name='python1'),
    path('java/', java, name='java'),
    path('java1/', java1, name='java1'),
    path('web/',web,name='web'),
    path('web1/', web1, name='web1'),
]
