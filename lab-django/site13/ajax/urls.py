from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax-random/', views.ajax_random, name='ajax_random')
]