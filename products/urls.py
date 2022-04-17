from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),   # this is like homepage for products app (http:....8000/products/)
    path('new', views.next) #like this we can add as many paths we want 
]