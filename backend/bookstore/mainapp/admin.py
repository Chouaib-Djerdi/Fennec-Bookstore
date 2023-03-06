from django.contrib import admin
from .models import Book,Author,Publisher
# Register your models here.

admin.site.register([Book,Author,Publisher])
