from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Scrapbook, Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.filter(status=2).order_by("-created_on")
    template_name = "scrapbook/index.html"
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.queryset, status=2).count()
        return context
    
def scrapbook_detail(request, slug):
    scrapbook = get_object_or_404(Scrapbook, slug=slug)
    posts = scrapbook.posts.filter(status=2).order_by("created_on")
    post_form = PostForm()
    
    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        return handle_post_request(request, scrapbook)

    context = {
        'scrapbook': scrapbook,
        'posts': page_obj,
        'post_form': post_form,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'scrapbook/scrapbook_detail.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ["scrapbook", 'title', 'image', 'status', 'content']
    template_name = 'scrapbook/post_form.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.scrapbook = get_object_or_404(
            Scrapbook, slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})

class PostUpdateView(UpdateView):
    model = Post
    fields = ["scrapbook", 'title', 'image', 'status', 'content']
    template_name = 'scrapbook/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'scrapbook/post_confirm_delete.html'
        
    def get_success_url(self):
        return reverse_lazy('scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})