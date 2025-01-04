from django.urls import path
from .views import home, page, about

urlpatterns = [
    path('', home, name='blog_home'),
    path('page/', page, name='blog_page'),
    path('about/', about, name='blog_about'),
]