from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

#what we want to diplay on any page is determined here by using diff functions
def index(request):
    items = Products.objects.all()
    return render(request,"index.html",{"products":items})
                  


def next(request):
    return HttpResponse("New Products")