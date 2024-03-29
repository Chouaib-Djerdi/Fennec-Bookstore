from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.BookListView.as_view()),
    path('books/<int:book_id>/comments/',views.CommentListCreateAPIView.as_view(),name='comment-list-create'),
    path('books/<int:book_id>/comments/<int:pk>/',views.CommentUpdateDeleteAPIView.as_view(),name='comment-update-delete'),
    
]
