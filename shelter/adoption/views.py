# we can use django.http or django.shortcuts to import HttpResponse, render etc
# - django shortscuts is a collection of helper function that are generally used in view function/classes. there are many shortcuts available in module django shortcuts
# => from django.http import HttpResponse


from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

books = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]

# anytime you create methods in view, you need  to go create the url in urls.py
def home(request):
    return render(request, 'home.html')

def show(request, id):
    book = list(filter(lambda book:book['id'] == id, books))
    data =  {'book':book[0]['id']}
    return render(request, 'show.html', data)

def books(request):
    data  = {'books': books}
    return render(request, 'books.html', data)

def authors(request):
    return render(request, 'author.html')
