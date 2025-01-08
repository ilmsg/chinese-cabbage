from django.contrib import admin
from .models import Book, Author, Authored

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Authored)