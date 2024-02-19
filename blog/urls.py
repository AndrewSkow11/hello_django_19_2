from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
                  # path('', NoteListView, name='list'),
                  path('create/', NoteCreateView.as_view(), name='create'),
                  # path('view/<int: pk>/', NoteListView.as_view(), name='view'),
                  # path('delete/<int: pk>', NoteDeleteView.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
