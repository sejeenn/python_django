from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer


# Create your views here.
def shop_index(request: HttpRequest):
    colors = {
        'red': '#FF0000',
        'green': '#008000',
        'yellow': '#FF0000',
        'blue': '#0000FF',
        'gray': '#C0C0C0',
    }
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
        "colors": colors,
    }
    return render(request, 'shopapp/shop-index.html', context=context)
