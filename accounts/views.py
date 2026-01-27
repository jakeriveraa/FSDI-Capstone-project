from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm

@login_required
def welcome(request):
    return render(request, 'account/welcome.html')

class UserLoginView(LoginView):
    template_name = 'account/login.html'

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})