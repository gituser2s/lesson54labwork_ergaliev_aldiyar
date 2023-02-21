from django.urls import path
from webapp.views.categories import category_add_view
from webapp.views.base import products_view
from webapp.views.products import product_view, product_add_view



urlpatterns = [
    path("", products_view, name='index'),
    path('products/<int:pk>', product_view, name='product_view'),
    #path('products/', products_view),
    path('products/add/', product_add_view, name='product_add_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    #path('categories/<int:pk>', category_view, name='category_view')
]
