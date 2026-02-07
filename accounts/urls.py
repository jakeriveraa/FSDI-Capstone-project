from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('welcome/', views.welcome, name='welcome'),
    path('myprofile/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:user_id>/', views.ProfileDetailView.as_view(), name='profile_details'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile_details'),
]
