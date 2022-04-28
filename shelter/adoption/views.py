# we can use django.http or django.shortcuts to import HttpResponse, render etc
# - django shortscuts is a collection of helper function that are generally used in view function/classes. there are many shortcuts available in module django shortcuts
# => from django.http import HttpResponse


from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

books = [
    {'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    {'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]

# => anytime I create methods in view,  I need  to go create the url in urls.py
def home(request):
    return render(request, 'adoption/home.html')


def show(request, id):
    book = list(filter(lambda book:book['id'] == id, books))
    data =  {'book':book[0]['id']}
    return render(request, 'adoption/show.html', data)


def books(request):
    data  = {'books': books}
    return render(request, 'adoption/books.html', data)


# @login_required
def authors(request):
    return render(request, 'adoption/author.html')
