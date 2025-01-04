from django.shortcuts import render
from django.http import JsonResponse
import random

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    return render(request, 'index.html')

def ajax_random(request):
    print(request.META.get('HTTP_X_REQUESTED_WITH'))
    
    if is_ajax(request=request):
        return JsonResponse({"random": random.randint(0, 100)})
    else:
        return render(request, 'ajax_random.html')


# def random_number(request):