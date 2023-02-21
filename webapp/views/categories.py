from django.shortcuts import render, redirect, reverse
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Categories



def category_add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'category_create.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }
    Categories.objects.create(**category_data)
    category = Categories.objects.all()
    return render(request, 'product_create.html', context={'category': category})

