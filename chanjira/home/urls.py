from django.urls import path
from .views import home, about, register, login, profile, setting, logout

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('setting/', setting, name='setting'),
    path('logout/', logout, name='logout'),
]