from django.shortcuts import render,redirect
from authapp.forms import UserCreationForm,RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('home')
        if form.is_valid():
            form.save()
            print('home')
            messages.success(request,"Account created successfully")
            return HttpResponseRedirect('/signup/')
    else:
        form = RegistrationForm()

    return render(request,'register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print('home')
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()
    return render(request,'home.html',{'form':form})


def index(request):
    return render(request,'login.html',{})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')
