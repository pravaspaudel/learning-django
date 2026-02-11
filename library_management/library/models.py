from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100) 
    isbn = models.CharField(max_length=20, unique=True)
    copies = models.PositiveIntegerField(default=1)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return f"{self.title} by {self.author}"

class Borrow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(default=timezone.now)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
