from django.urls import path
from . import views

urlpatterns = [
    # we give the name arguments to paths so we can use this urls in other  parts our the app .
    # we have to create a list of url paths
    # the path need  mandatory parameters ie routes and HTTP object s
    path('', views.home, name='adoption-home'),
    path('authors/', views.authors, name='adoption-authors'),
    path('books/', views.books, name='adoption-books'),
    # in the path below we use a path converter provided by django to  to access single book by id in the browser like so http://127.0.0.1:8000/adoption/books/1/
    path('books/<int:id>/', views.show, name='adoption-books')
]
