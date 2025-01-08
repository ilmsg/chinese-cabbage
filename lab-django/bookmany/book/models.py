from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author', through='Authored')
    
    def __str__(self):
        print(self.authors)
        return self.title
        # return f"{self.title}, {','.join([author for author in [("a"),("b")]])}"
    
class Author(models.Model):
    title = models.CharField(max_length=200)
    books = models.ManyToManyField('Book', through='Authored')
    
    def __str__(self):
        return self.title
    
class Authored(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.book.title}, {self.author.title}"