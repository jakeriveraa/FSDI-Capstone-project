from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    if request.method == 'POST':
        # Handle form submission here (not implemented)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful submission

    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})