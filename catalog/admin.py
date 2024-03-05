from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('nomination', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number', 'nomination')
