from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,"Username already in use")
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,"Email already in use")
               return redirect('register')
           else:
               user=User.objects.create_user(username=username,password=password,email=email)
               user.save()
               return redirect('login')
        else:
            messages.info(request,"Password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('logged')
        else:
            messages.info(request,"Invalid Login Credentials")
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def forms(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request,'forms.html')

def success(request):
    return render(request,'success.html')

def email(request):
    return render(request,'email.html')

def logged(request):
    return render(request,'logged.html')