from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination')
    # list_filter = (список_полей_для_фильтрации)
    # search_fields = (список_полей_для_поиска)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('nomination', 'description')
