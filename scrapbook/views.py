from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Scrapbook, Post
from .forms import PostForm, ScrapbookForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class ScrapbookListView(generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context
    
class ScrapbookDetailView(generic.DetailView):
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_detail.html'
    context_object_name = 'scrapbook'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scrapbook = self.get_object()
        posts = scrapbook.posts.all()
        ordering = ["-created_on"]
        post_form = PostForm()
        
        # Pagination
        paginator = Paginator(posts, 6)  # Show 6 posts per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context.update({
            'posts': page_obj,
            'post_form': post_form,
            'is_paginated': page_obj.has_other_pages(),
            'page_obj': page_obj,
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return handle_post_request(request, self.object)

class ScrapbookCreateView(CreateView):
    model = Scrapbook
    form_class = ScrapbookForm
    template_name = 'scrapbook/scrapbook_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.slug})


class ScrapbookUpdateView(UpdateView):
    model = Scrapbook
    form_class = ScrapbookForm
    template_name = 'scrapbook/scrapbook_form.html'
    
    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.slug})
    
class ScrapbookDeleteView(DeleteView):
    model = Scrapbook
    template_name = 'scrapbook/confirm_delete.html'
        
    def get_success_url(self):
        return reverse_lazy('home')

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    
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
    
    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)

    def get_success_url(self):
        return reverse_lazy('scrapbook:post_detail', kwargs={'scrapbook_slug': self.object.scrapbook.slug, 'post_slug': self.object.slug})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'scrapbook/confirm_delete.html'
        
    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail', kwargs={'slug': self.object.scrapbook.slug})


# PostDetailView extends generic.DetailView
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'scrapbook/post_detail.html'
    
    def get_object(self):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_slug = self.kwargs['post_slug']
        return get_object_or_404(Post, slug=post_slug, scrapbook__slug=scrapbook_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scrapbook'] = self.object.scrapbook
        return context

def create_scrapbook(request):
    if request.method == 'POST':
        form = ScrapbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('scrapbook:home'))
    else:
        form = ScrapbookForm()
    return render(request, 'scrapbook/scrapbook_form.html', {'form': form})