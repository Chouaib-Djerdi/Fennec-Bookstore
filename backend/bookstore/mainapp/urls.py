from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.mainpage,name='main-page'),
    path('book_detail/<int:pk>',views.bookdetailpage,name='book-detail'),
    path('author_detail/<int:pk>',views.authordetailpage,name='author-detail'),
    path('book_list/',views.booklistpage,name='book-list'),
    path('search/',views.searchbar,name='searchbar'),
]
