from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def page(request):
    return render(request, 'blog/page.html')

def about(request):
    return render(request, 'blog/about.html')