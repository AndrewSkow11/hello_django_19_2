from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contacts, product

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', product, name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)