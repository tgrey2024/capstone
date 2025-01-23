from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Scrapbook, Post, SharedAccess
from .forms import PostForm, ScrapbookForm, ShareContentForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import logging
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

class ScrapbookListView(generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context
    
class ScrapbookMyListView(LoginRequiredMixin, generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_mylist.html"
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the user's own scrapbooks
        queryset = Scrapbook.objects.filter(author=self.request.user)
        return queryset

class ScrapbookSharedListView(LoginRequiredMixin, generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_sharedlist.html"
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the shared scrapbooks
        queryset = Scrapbook.objects.filter(sharedaccess__user=self.request.user).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shared_scrapbooks'] = self.get_queryset()
        return context

    
class ScrapbookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_detail.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook = super().get_object(queryset)
        if scrapbook.status != 2 and scrapbook.author != self.request.user:
            if not SharedAccess.objects.filter(user=self.request.user, scrapbook=scrapbook).exists():
                raise PermissionDenied("You do not have permission to view this scrapbook.")
        return scrapbook

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return HttpResponseForbidden("You do not have permission to view this scrapbook.")

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
        
        # Get shared access for the current user and scrapbook
        sharedaccess = SharedAccess.objects.filter(user=self.request.user, scrapbook=scrapbook).exists()
        
        context.update({
            'posts': page_obj,
            'post_form': post_form,
            'is_paginated': page_obj.has_other_pages(),
            'page_obj': page_obj,
            'sharedaccess': sharedaccess,
            'permission_denied': not sharedaccess and scrapbook.author != self.request.user and scrapbook.status != 2,
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return handle_post_request(request, self.object)
    
def handle_post_request(request, scrapbook):
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.author = request.user
        post.scrapbook = scrapbook
        post.save()
        messages.success(request, "Post created successfully.")
    else:
        messages.error(request, "Post creation failed.")
    return redirect(reverse('scrapbook:scrapbook_detail', kwargs={'slug': scrapbook.slug}))

class ScrapbookCreateView(LoginRequiredMixin, CreateView):
    model = Scrapbook
    form_class = ScrapbookForm
    template_name = 'scrapbook/scrapbook_form.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Scrapbook created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_scrapbook_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context


class ScrapbookUpdateView(LoginRequiredMixin, UpdateView):
    model = Scrapbook
    form_class = ScrapbookForm
    template_name = 'scrapbook/scrapbook_form.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        messages.success(self.request, "Scrapbook updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_scrapbook_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        return context
    
class ScrapbookDeleteView(LoginRequiredMixin, DeleteView):
    model = Scrapbook
    template_name = 'scrapbook/confirm_delete.html'
    login_url = '/accounts/login/'

    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        scrapbook_id = self.kwargs['scrapbook_id']
        return get_object_or_404(Scrapbook, id=scrapbook_id, slug=scrapbook_slug)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Scrapbook deleted successfully.")
        return response
    
    def get_success_url(self):
        return reverse_lazy('my_scrapbook_list')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    login_url = '/accounts/login/'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['scrapbook'] = get_object_or_404(Scrapbook, slug=self.kwargs['slug'])
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.scrapbook = get_object_or_404(
            Scrapbook, slug=self.kwargs['slug'])
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    login_url = '/accounts/login/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['scrapbook'] = get_object_or_404(Scrapbook, slug=self.kwargs['slug'])
        return kwargs

    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Post updated successfully.")
        return response
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'scrapbook/confirm_delete.html'
    login_url = '/accounts/login/'

    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Post deleted successfully.")
        return response

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail', kwargs={'slug': self.object.scrapbook.slug})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'scrapbook/post_detail.html'
    login_url = '/accounts/login/'

    def get_object(self):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_slug = self.kwargs['post_slug']
        post = get_object_or_404(Post, slug=post_slug, scrapbook__slug=scrapbook_slug)
        if post.status != 2 and post.author != self.request.user:
            if not SharedAccess.objects.filter(user=self.request.user, post=post).exists():
                raise PermissionDenied("You do not have permission to view this post.")
        return post
    
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

@login_required
def share_content(request):
    scrapbook_id = request.GET.get('scrapbook_id')
    post_id = request.GET.get('post_id')
    
    if request.method == 'POST':
        form = ShareContentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                if scrapbook_id:
                    scrapbook = Scrapbook.objects.get(id=scrapbook_id)
                    # Create a SharedAccess entry for the scrapbook
                    SharedAccess.objects.create(user=user, scrapbook=scrapbook, shared_by=request.user)
                    # Share all posts within the scrapbook
                    posts = Post.objects.filter(scrapbook=scrapbook)
                    for post in posts:
                        SharedAccess.objects.create(user=user, scrapbook=scrapbook, post=post, shared_by=request.user)
                    messages.success(request, "Scrapbook and its posts shared successfully.")
                else:
                    messages.error(request, "Scrapbook does not exist.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
            except (Scrapbook.DoesNotExist, Post.DoesNotExist):
                messages.error(request, "Scrapbook does not exist.")
        return redirect('home')
    else:
        form = ShareContentForm(initial={'scrapbook_id': scrapbook_id, 'post_id': post_id})
    return render(request, 'scrapbook/share_content.html', {'form': form})