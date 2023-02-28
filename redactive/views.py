from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1==pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
        
        if  len(username)>10 or len(username)<10:    
            messages.info(request,"phone Number Must be 10 Digits")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                redirect('/signup')

        except Exception as indentifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')


        except Exception as indentifier:
            pass


        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"user is Created Please Login")
        return redirect('/login')     



    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('userumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/login')



    return render(request,"handlelogin.html")


