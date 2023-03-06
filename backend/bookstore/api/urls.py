from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.BookListCreateView.as_view()),
]
