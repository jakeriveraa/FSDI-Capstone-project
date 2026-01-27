from django.contrib import admin
from .models import Note, Category, Comment
# Register your models here.
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Comment)
