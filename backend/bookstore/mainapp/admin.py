from django.contrib import admin
from .models import Book,Author,Publisher,Wishlist
# Register your models here.

admin.site.register([Book,Author,Publisher,Wishlist])
