from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import ProfileForm, CustomSingUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# class ProfileView(DetailView):
#     model = UserProfile
#     template_name = 'profile.html'
#     context_object_name = 'profile'



class SignUpView(CreateView):
    form_class = CustomSingUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class ProfileView(LoginRequiredMixin, DetailView): # LoginRequiredMixin - to access users that already login, DetailView - we need to see only about 1 user
    model = UserProfile #python bull-in model
    template_name = 'profile.html' # template_name = profile.html
    context_object_name = 'profile_context' # take object to template

    def get_object(self, queryset=None): # take loggedin user
 
        return self.request.user #self.query.set - access to user
