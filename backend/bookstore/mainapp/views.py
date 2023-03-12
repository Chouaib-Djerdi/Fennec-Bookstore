from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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
    

@login_required
def add_to_wishlist(request,pk):
    book = get_object_or_404(models.Book, pk=pk)
    wishlist, created = models.Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(book)
    return redirect('/wishlist/')

@login_required
def wishlist(request):
    wishlist, created = models.Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.products.all()

    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, 'mainapp/wishlist.html', context)

@login_required
def remove_from_wishlist(request, pk):
    if request.method == "POST":    
        # wishlist = models.Wishlist.objects.get(user=request.user)
        # wishlist.items.delete(item)
        
        models.Wishlist.objects.filter(user=request.user,products=models.Book.objects.get(pk=pk)).delete()
        return redirect('/wishlist/')
    return redirect('/')