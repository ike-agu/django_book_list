from django.urls import path
from . import views

urlpatterns = [
    # we give the name arguments to path so we can use this urls in other  parts our the app .
    # we have to create a list of url paths
    # the path need  mandatory parameters ie routes and HTTP object s
    path('', views.home, name='adoption-home'),
    path('authors/', views.authors, name='adoption-authors'),
    path('books/', views.show, name='adoption-show'),
    path('books/<int:id>/', views.show, name='adoption-show')
    ]
