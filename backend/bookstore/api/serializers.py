from rest_framework import serializers
from mainapp.models import Publisher,Author,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
