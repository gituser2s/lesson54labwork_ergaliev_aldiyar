from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Products, Categories
from django.shortcuts import render


def products_view(request: WSGIRequest):
    products = Products.objects.all()
    categories = Categories.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context=context)
