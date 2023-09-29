from django.shortcuts import render


def index(request):
    return render(request, 'authorize/login.html')

def register(request):
    return render(request, 'authorize/registration.html')
