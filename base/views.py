
from todu_list import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
def home(request):
    return render(request,"authenticate/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['password']
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your Account has been successfully created 😊😊")
        #email sending
       
        return redirect("login")
        
    return render(request,"authenticate/signup.html")
def login(request):
    if request.method=="POST":
        
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            auth_login(request,user)
            fame=user.first_name

            # Redirect to a success page.
           
            return render(request,"authenticate/index.html",{"fame":fame})
            
            
        else:
            messages.error(request,"Bad creadintials")
     
            return redirect("home")
    return render(request,"authenticate/signin.html")
        # Return an 'invalid login' error message.
        
    #     if user is not None:
    #         login( request,user)
    #         fname=user.first_name
    #         return render(request,"authenticate/index.html",{"fname":fname})
    #     else:
    #         messages.error(request,"Bad creadintials")
    #         return redirect("home")
    # return render(request,"authenticate/signin.html")
def logout(request):
    auth_logout(request)
    messages.success(request,"Your Successfully loggodout")
    return redirect("home")
    
