from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Book

# Create your models here.

class Comment(models.Model):
    BOOK_RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    rating = models.IntegerField(choices=BOOK_RATING_CHOICES, blank=True,null=True)

    def __str__(self):
        return f'{self.user.username}\'s comment on {self.book.title}'
    
    class Meta:
        unique_together = ('user', 'book',)

