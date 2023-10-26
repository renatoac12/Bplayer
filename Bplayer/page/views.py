from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signIn(request):
    return render(request, 'registro.html')

def logIn(request):
    return render(request, 'login.html')
