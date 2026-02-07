from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Comment
from .forms import NoteForm
from django.urls import reverse_lazy


"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""


# create your views here.

class NoteListView(ListView):
    model = Note
    template_name = "notes/list.html"


class NoteCreateView(CreateView):
    model = Note
    template_name = "notes/create.html"
    form_class = NoteForm
    success_url = reverse_lazy("notes_list")


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/detail.html"

    # getting the data
    def get_context_data(self, **kwargs):
        # get the base functionality
        context = super().get_context_data(**kwargs)
        # read and the comments related to the note
        note = self.object
        comments = Comment.objects.filter(note=note).select_related('author').order_by("-created_at")
        
        # Debug print
        for comment in comments:
            print(f"Author: {comment.author.username}")
            print(f"Has profile: {hasattr(comment.author, 'profile')}")
            if hasattr(comment.author, 'profile'):
                print(f"Has picture: {comment.author.profile.picture}")
        
        context['comments'] = comments
        return context


def create_comment(request):
    # get data
    note_id = request.POST.get("note_id")
    content = request.POST.get("content")

    # create comment
    note = Note.objects.get(id=note_id)
    
    comment = Comment.objects.create(
        note=note,
        content=content,
        author=request.user
    )
    comment.save()
    return redirect("notes_detail", pk=note_id)