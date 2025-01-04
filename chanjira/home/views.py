from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def register(request):
    return render(request, 'home/register.html')

def login(request):
    return render(request, 'home/login.html')

def profile(request):
    return render(request, 'home/profile.html')

def setting(request):
    return render(request, 'home/setting.html')

def logout(request):
    return render(request, 'home/logout.html')