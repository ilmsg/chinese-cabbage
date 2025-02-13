from django.db import models

class Lang(models.Model):
    title = models.CharField(max_length=200)
    
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    lang = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True)
    
class Instance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)