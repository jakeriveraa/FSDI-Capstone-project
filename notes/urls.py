from django.urls import path
from .views import NoteListView, NoteCreateView, NoteDetailView
from . import views


urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('create/', NoteCreateView.as_view(), name='notes_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='notes_detail'),
    path('create_comment/', views.create_comment, name='create_comment'),
]