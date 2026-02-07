from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm

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
            Profile.objects.create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile_details.html'
    context_object_name = 'profile'

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            profile, created = Profile.objects.get_or_create(user_id=user_id)
        else:
            profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.user != request.user:
            return redirect('profile_details', user_id=profile.user.id)
        return super().dispatch(request, *args, **kwargs)