from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
# def indexView(request):
#     return render(request, 'base.html')

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
class PostEditView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')