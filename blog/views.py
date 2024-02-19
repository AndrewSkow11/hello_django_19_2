from django.views.generic import CreateView, ListView, DetailView, DeleteView

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


class NoteDeleteView(DeleteView):
    model = Note


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
