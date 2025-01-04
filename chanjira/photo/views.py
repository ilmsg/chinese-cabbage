from django.shortcuts import render

def home(request):
    return render(request, 'photo/home.html')

def album(request):
    return render(request, 'photo/album.html')

def album_view(request, album_id):
    return render(request, 'photo/album_view.html', {'album_id': album_id})