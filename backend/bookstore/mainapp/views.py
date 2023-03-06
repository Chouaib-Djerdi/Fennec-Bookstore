from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def mainpage(request):
    books = models.Book.objects.all()
    
    return render(request,'mainapp/main.html',{'books':books})

def bookdetailpage(request,pk):
    book = models.Book.objects.get(pk=pk)
    alike_books = models.Book.objects.filter(genre=book.genre).exclude(pk=pk)

    return render(request,'mainapp/book_detail.html',{'book':book,'alike_books':alike_books})

def authordetailpage(request,pk):
    book = models.Book.objects.get(pk=pk)
    authorbooks = models.Book.objects.filter(author=book.author)
    return render(request,'mainapp/author_detail.html',{'author':book.author,'authorbooks':authorbooks})

def booklistpage(request):
    books = models.Book.objects.all()
    paginator = Paginator(books,2)
    page_nbr = request.GET.get('page')
    page_obj = paginator.get_page(page_nbr)
    nbr = 'a' * page_obj.paginator.num_pages
    return render(request,'mainapp/trend.html',{'page_obj':page_obj,'nbr':nbr})

def searchbar(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        books = models.Book.objects.filter(Q(title__icontains=searched) | Q(description__icontains=searched))
        
        return render(request,'mainapp/searchbar.html',context={'searched':searched,'books':books})
    else:
        return render(request,'mainapp/searchbar.html')