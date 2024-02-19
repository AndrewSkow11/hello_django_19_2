from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)