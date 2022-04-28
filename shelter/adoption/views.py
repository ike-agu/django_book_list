from django.shortcuts import HttpResponse

# Create your views here.

books = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]


def home(request):
    return HttpResponse("<h1>List of book to view </h1>")

def authors(request):
    return HttpResponse(f"<h1>List of Book authors</h1>")
