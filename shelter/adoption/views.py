# we can use django.http or django.shortcuts to import HttpResponse
# - django shortscuts is a collection of helper function that are generally used in view function/classes. there are many shortcuts available in module django shortcuts
# => from django.http import HttpResponse

from django.shortcuts import HttpResponse

# Create your views here.

books = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]

# anytime you create methods in view, you need  to go create the url in urls.py
def home(request):
    return HttpResponse("<h1>List of book to view </h1>"
    f"<h3>The books in our list are {len(books)} in total </h3>"
    )

def show(request, id):
    book = list(filter(lambda book:book['id'] == id, books))
    return HttpResponse(
        f"<h3>This page is for book number with id {id}</h3>"
        f"<p>The book  name is {book[0]['title']}.</p>"
    )

def authors(request):
    return HttpResponse(f"<h1>List of Book authors</h1>")
