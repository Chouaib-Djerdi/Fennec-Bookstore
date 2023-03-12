from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.mainpage,name='main-page'),
    path('book_detail/<int:pk>',views.bookdetailpage,name='book-detail'),
    path('author_detail/<int:pk>',views.authordetailpage,name='author-detail'),
    path('book_list/',views.booklistpage,name='book-list'),
    path('search/',views.searchbar,name='searchbar'),
    path('item/<int:pk>',views.add_to_wishlist,name='wishlist-add'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('item/<int:pk>',views.remove_from_wishlist,name='wishlist-remove'),
]
