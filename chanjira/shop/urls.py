from django.urls import path
from .views import home, page, about

urlpatterns = [
    path('', home, name='shop_home'),
    path('page/', page, name='shop_page'),
    path('about/', about, name='shop_about'),   
]
