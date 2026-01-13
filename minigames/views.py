from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def placeholder(request):
    return render(request, 'minigames/minigames.html')  # create this template
