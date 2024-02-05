from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('nomination', 'description')
