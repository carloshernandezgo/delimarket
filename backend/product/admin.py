from django.contrib import admin

from product.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    ordering = ('id',)


admin.site.register(Product, ProductAdmin)
