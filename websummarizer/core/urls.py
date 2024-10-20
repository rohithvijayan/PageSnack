from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [
  path("api/home/",home,name='home'),
  path("api/quicksearch/",quick_search,name='quicksearch'),
]
