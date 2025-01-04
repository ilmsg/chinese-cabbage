from django.urls import path
from .views import home, album, album_view

urlpatterns = [
    path('', home, name='photo_home'),
    path('album/', album, name='photo_album'),
    path('album/<str:album_id>', album_view, name='photo_album_view'),
]
