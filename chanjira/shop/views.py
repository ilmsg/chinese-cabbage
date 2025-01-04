from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

def page(request):
    return render(request, 'shop/page.html')

def about(request):
    return render(request, 'shop/about.html')