from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Book
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username}\'s comment on {self.book.title}'