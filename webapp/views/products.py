from django.shortcuts import render, redirect, reverse
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Products, Categories
from django.shortcuts import get_object_or_404


def product_add_view(request: WSGIRequest):
    if request.method == "GET":
        category = Categories.objects.all()
        return render(request, 'product_create.html', context={'category': category})
    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category': Categories.objects.get(id=request.POST.get('category_id')),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
    }
    #user_products.category = categories.objects.get(grp_categorie__category='category')
    print(product_data)
    product = Products.objects.create(**product_data)
    return redirect('product_view', kwargs={'pk': product.pk, 'product': product})


def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)



