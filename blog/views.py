from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from blog.models import Note


# Create your views here.
class NoteCreateView(CreateView):
    model = Note
    fields = [
        'header',
        'slug',
        'content',
        'preview',
        'is_published',
    ]
    success_url = reverse_lazy('blog:list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = [
        'header',
        'slug',
        'content',
        'preview',
        'is_published',
    ]
    success_url = reverse_lazy('blog:list')

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('blog:list')



class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
    success_url = reverse_lazy('blog:list')

