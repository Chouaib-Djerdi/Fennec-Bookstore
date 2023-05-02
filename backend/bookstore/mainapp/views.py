from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .utils import cookieCart,cartData,guestOrder
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.


def mainpage(request):
    books = models.Book.objects.all()
    publishers = models.Publisher.objects.all()

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    books = models.Book.objects.all()
    context = {'books': books, 'cartItems': cartItems, 'publishers': publishers}

    return render(request, 'mainapp/fen.html',context)


def bookdetailpage(request,pk):
    book = models.Book.objects.get(pk=pk)
    alike_books = models.Book.objects.filter(genre=book.genre).exclude(pk=pk)

    return render(request,'mainapp/secondpage.html',{'book':book,'alike_books':alike_books})

def authordetailpage(request,pk):
    book = models.Book.objects.get(pk=pk)
    authorbooks = models.Book.objects.filter(author=book.author)
    return render(request,'mainapp/author_detail.html',{'author':book.author,'authorbooks':authorbooks})

def booklistpage(request):
    books = models.Book.objects.all()
    paginator = Paginator(books,3)
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
    
def category(request):
    categories = []
    for i in models.Book.GENRE_CHOICES:
        categories.append(i[0])

    nbr = len(categories)
    context = {
        'categories':categories,
        'nbr':nbr,
    }
    return render(request,'mainapp/category.html',context)
    

@login_required
def add_to_wishlist(request,pk):
    book = get_object_or_404(models.Book, pk=pk)
    wishlist, created = models.Wishlist.objects.get_or_create(user=request.user)
    # if wishlist.products.get(pk=pk):

    wishlist.products.add(book)
    return redirect('/')

@login_required
def wishlist(request):
    wishlist, created = models.Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.products.all()
    # items_nbr = wishlist.products.all().count()
    context = {
        'wishlist_items': wishlist_items,
        
    }
    return render(request, 'mainapp/wishlist.html', context)

@login_required
def remove_from_wishlist(request, pk):
    if request.method == "POST":    
        # wishlist = models.Wishlist.objects.get(user=request.user)
        # wishlist.items.delete(item)
        wishlist = models.Wishlist.objects.get(user=request.user)
        book = models.Book.objects.get(pk=pk)
        wishlist.products.remove(book)
        wishlist.save()
        # models.Wishlist.objects.filter(user=request.user,products=models.Book.objects.get(pk=pk)).delete()
        return redirect('/wishlist/')
    return redirect('/')

def cart(request):
    # cart, created = models.Order.objects.get_or_create(customer=request.user.customer)
    # cart_items = cart.orderitem_set.all()

    # return render(request,'mainapp/cart.html',context={'cart_items':cart_items,'cart':cart})
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'cartItems':cartItems, 'cart':order, 'items':items}
    return render(request, 'mainapp/cart.html', context)
    

    
def updateitem(request):
    data = json.loads(request.body)
    productId  = data['productId']
    action = data['action']
    print('ProductId :',productId)
    print('Action :',action)

    customer = request.user.customer
    product = models.Book.objects.get(id=productId)
    order, created = models.Order.objects.get_or_create(customer=customer,complete=False)
    orderitem, created = models.OrderItem.objects.get_or_create(order=order, product=product) 
    
    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
        
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()


    return JsonResponse('Item was added',safe=False) 


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }

    return render(request, 'mainapp/checkout.html', context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if True:
		models.ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)