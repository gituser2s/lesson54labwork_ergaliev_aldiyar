from django.contrib import admin
from webapp.models import Products, Categories

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'price', 'image', 'created_at')
    list_filter = ('id', 'title', 'description', 'category', 'price', 'image', 'created_at')
    search_fields = ('title', 'description', 'category', 'price', 'image')
    fields = ('title', 'description', 'category', 'price', 'image', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_filter = ('id', 'title', 'description', 'created_at')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CategoriesAdmin)
