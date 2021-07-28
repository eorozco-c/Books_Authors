from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_book',views.addBook),
    path('books/<int:idbook>',views.books),
    path('add_author',views.addAuthor),
    path('author',views.authorIndex),
    path('add_new_author',views.addNewAuthor),
    path('author/<int:idauthor>',views.authors),
    path('add_new_book',views.addNewBook),
]