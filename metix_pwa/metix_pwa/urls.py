"""metix_pwa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.http import HttpResponse
from django.urls import path
from django.contrib import admin
from django.shortcuts import render

from google_home.command import send_broadcast




def google_home_command(request):

    return render(request, 'main/google_home_commands.html')

def call_google_home(request):
    if request.method == 'GET':
        command = ' '.join(request.GET['command'].split('_'))
        send_broadcast(command)
    return HttpResponse()

def index(request):
    print("test")
    return render(request,"main/index.html")

def base_layout(request):
    template='base.html'
    return render(request,template)


urlpatterns = [

    url('', include('pwa.urls')),
    url(r'^call_google_home/$', call_google_home), 
    url(r'^commands/$', google_home_command), 
    url(r'^admin/', admin.site.urls),
    url(r'^base_layout' , base_layout),
    url(r'^patient/' , include('patient.urls')),
    url('accounts/', include('django.contrib.auth.urls')), 
    path('', index),

]
