from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from buttonpython.facerec import verify
from buttonpython.take_photo_store_in_db import takephoto
from buttonpython.faces_train import trainit

def button(request):
    return render(request,'registration_main.html', {"data":"false"})

def output(request):
    data=requests.get("https://reqres.in/api/users")
    print(data.text)
    data=data.text
    return render(request, 'registration_main.html', {'data':data})

def external(request):
    name = verify()
    return render(request, 'registration_main.html', {"data":"true", "name":name})

def logg(request):
   data=requests.get("https://reqres.in/api/users")
#    print(data.text)
   data = data.text

   return render(request, 'projfile1.html', {'data':data})

def welcome(request):

    return render(request, 'welcome.html')

def create(request):
    return render(request, 'loginconc.html')

def new_photo(request):
    try:
        takephoto()
    except Exception as e:
        print(e)
    return render(request, 'loginconc.html')    