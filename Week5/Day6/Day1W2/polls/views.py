from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views import generic
from django.forms.models import BaseModelForm
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# CRUD - CREATE - RETRIEVE - UPDATE - DELETE

@login_required(login_url = reverse_lazy('login'))
def a_view(request):
    ...



class PostCreateView(LoginRequiredMixin, generic.CreateView):

    login_url = reverse_lazy('login')
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")

    def get_initial(self) -> Dict[str, Any]:
        user = self.request.user
        profile = user.profile
        initial_data = {'author': profile,
                        'date_created': date.today()}
        return initial_data

    # def get_form_class(self) -> type[BaseModelForm]:
    #     form = super().get_form_class()
    #     user = self.request.userprofile 
    #     profile = user.profile

    #     form = form(initial={'author': profile})
    #     return form

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):

    login_url = reverse_lazy('login')
    template_name = 'update_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")





class PostListView(generic.ListView):

    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()
        print("User:", self.request.user)
        return context

class PostView(generic.DetailView):

    template_name = 'post.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        return context
    