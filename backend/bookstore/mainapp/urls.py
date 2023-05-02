from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.mainpage,name='main-page'),
    path('book_detail/<int:pk>',views.bookdetailpage,name='book-detail'),
    path('author_detail/<int:pk>',views.authordetailpage,name='author-detail'),
    path('book_list/',views.booklistpage,name='book-list'),
    path('search/',views.searchbar,name='searchbar'),
    path('category/',views.category,name='category'),
    path('item/<int:pk>',views.add_to_wishlist,name='wishlist-add'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('wishlist/remove/<int:pk>/',views.remove_from_wishlist,name='wishlist-remove'),
    path('cart/',views.cart,name='cart'),
    path('update_item/',views.updateitem,name='update_item'),
    path('checkout/',views.checkout,name='checkout'),
    path('process_order/',views.processOrder,name='process_order'),

]
