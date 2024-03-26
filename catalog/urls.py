from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ProductView,
    ProductUpdateView,
    ContactView,
    ProductDetailView,
    ProductCreateView,
    ProductDeleteView,
    categories,
    category_products,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("view/<int:pk>", cache_page(60)(ProductDetailView.as_view()),
         name="view"),
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("update/<int:pk>", ProductUpdateView.as_view(),
         name="update_product"),
    path("delete/<int:pk>", ProductDeleteView.as_view(),
         name="delete_product"),
    path("categories/", categories, name="categories"),
    path("<int:pk>/products", category_products, name="category_products"),
]
