
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    Address = models.TextField()
    MembershipDate = models.DateField(blank=True, null=True)
    Borrowed_books = models.ManyToManyField('Book', through='BorrowedBooks', related_name='borrowers')

    def __str__(self):
        return self.username

class Book(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    PublishedDate = models.DateField()
    ISBN = models.CharField(max_length=255, unique=True)
    Genre = models.CharField(max_length=255)
    Details = models.OneToOneField('BookDetails', on_delete=models.CASCADE, related_name='book_details',null = True, blank = True)

    def __str__(self):
        return self.Title

class BookDetails(models.Model):
    Book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_details')
    Number_of_pages = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Book.Title}"

class BorrowedBooks(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Borrow_date = models.DateField()
    Return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.User.username} [{self.Book.Title}]"