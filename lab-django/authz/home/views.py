from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class OpenView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class ManualProtect(View):
    def get(self, request):
        print(request.user)
        if not request.user.is_authenticated:
            login_url = reverse('login')
            return redirect(login_url)
        return render(request, 'home.html')