from rest_framework import serializers
from mainapp.models import Publisher,Author,Book
from django.contrib.auth.models import User
from .models import Comment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id','user','book','content','rating','likes','dislikes','created_at','updated_at']

