from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login
from django.views.generic import UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import BlogPost, Category
from .forms import RegisterForm  # Register form

# Home view with search, filter, and pagination
def blog_home(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    posts = BlogPost.objects.select_related('author').prefetch_related('categories').order_by('-created_at')

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    if category_id:
        posts = posts.filter(categories__id=category_id)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'selected_category': category_id,
        'categories': Category.objects.all(),
    }

    if request.headers.get('HX-Request'):  # HTMX request
        return render(request, 'blog/_post_list.html', context)
    return render(request, 'blog/home.html', context)

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# View a single post
class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'

# Author-only post editing view
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'categories']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Author-only post deletion view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
