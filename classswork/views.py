from django.shortcuts import render
from django.http import HttpResponse
from . import settings

def index_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def contact_page(request):
    return render(request,'contact.html')

def shop_page(request):
    return render(request,'shop.html')


def shop_single_page(request):
    return render(request,'shop-single.html')


