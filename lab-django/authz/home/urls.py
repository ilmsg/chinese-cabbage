from django.urls import path
from . import views

urlpatterns = [
    path('', views.OpenView.as_view()),
    path('protect', views.ManualProtect.as_view()),
    path('login', views.OpenView.as_view(), name='login')
]
