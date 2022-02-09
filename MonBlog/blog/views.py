from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.


class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class CreateBlogPost(CreateView):
    template_name = 'create_post.html'
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nouveau Post"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateBlogPost(UpdateView):
    template_name = 'create_post.html'
    model = BlogPost
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modifier Le Post"
        return context


@method_decorator(login_required, name='dispatch')
class DeleteBlogPost(DeleteView):
    template_name = 'delete_post.html'
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('home')


class DetailBlogPost(DetailView):
    template_name = 'detail_post.html'
    model = BlogPost
    context_object_name = 'post'