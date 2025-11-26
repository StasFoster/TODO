from django.shortcuts import render
from django.contrib.auth import login

from . import forms

def welcome(request):
    if request.user.is_authenticated:
        pass
    return render(request, "Registration/index.html")

def register(request):
    if request.method == "POST":
        f = forms.Registration_Form(request.POST)
        if f.is_valid():
            user = f.save()
            login(request, user)
            pass
            
    form = forms.Registration_Form()
    return render(request, "Registration/registr.html", {"form":form, "isLogin":False})
    

def sign_in(request):
    if request.method == "POST":
        pass
    form = forms.Login_Form()
    return render(request, "Registration/registr.html", {"form":form, "isLogin":True})