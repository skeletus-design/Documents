from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html') 
    else:
        return redirect('/sign_in')

def login_(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'authorize/login.html')

def register(request):
    return render(request, 'authorize/registration.html')

