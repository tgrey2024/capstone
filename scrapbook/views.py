from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Scrapbook, Post, SharedAccess
from .forms import PostForm, ScrapbookForm, ShareContentForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

def custom_csrf_failure_view(request, reason=""):
    return render(request, '403_csrf.html', status=403)

def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

class ScrapbookListView(generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/index.html"
    paginate_by = 6  # Show 6 scrapbooks per page

    def get_queryset(self):
        # Filter scrapbooks to only show public scrapbooks
        queryset = Scrapbook.objects.filter(status=2).order_by('-created_on')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context
    
class ScrapbookMyListView(LoginRequiredMixin, generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_mylist.html"
    paginate_by = 6  # Show 6 scrapbooks per page
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the user's scrapbooks
        queryset = Scrapbook.objects.filter(author=self.request.user).order_by('-created_on')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context

class ScrapbookSharedListView(LoginRequiredMixin, generic.ListView):
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_sharedlist.html"
    paginate_by = 6  # Show 6 scrapbooks per page
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the shared scrapbooks
        queryset = Scrapbook.objects.filter(sharedaccess__user=self.request.user).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context

    
class ScrapbookDetailView(generic.DetailView):
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_detail.html'

    def get_object(self, queryset=None):
        scrapbook = super().get_object(queryset)
        if scrapbook.status != 2 and scrapbook.author != self.request.user:
            if not self.request.user.is_authenticated or not SharedAccess.objects.filter(user=self.request.user, scrapbook=scrapbook).exists():
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
        paginator = Paginator(posts, 6)  # Show 6 posts per page

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ordering = ["-created_on"]
        context.update({
            'scrapbook': scrapbook,
            'page_obj': page_obj,
            'posts': page_obj.object_list,
            'is_paginated': page_obj.has_other_pages(),
            'ordering': ordering,
        })
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

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
        return reverse_lazy('scrapbook:scrapbook_detail', kwargs={'slug': self.object.slug})
    
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
        kwargs['scrapbook'] = get_object_or_404(Scrapbook, slug=self.kwargs['scrapbook_slug'])
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.scrapbook = get_object_or_404(
            Scrapbook, slug=self.kwargs['scrapbook_slug'])
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        context['scrapbook'] = get_object_or_404(Scrapbook, slug=self.kwargs['scrapbook_slug'])
        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.scrapbook = get_object_or_404(
            Scrapbook, slug=self.kwargs['scrapbook_slug'])
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail',
                            kwargs={'slug': self.object.scrapbook.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'edit'
        context['scrapbook'] = get_object_or_404(Scrapbook, slug=self.kwargs['scrapbook_slug'])
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'scrapbook/confirm_delete.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_id = self.kwargs['post_id']
        try:
            return get_object_or_404(Post, id=post_id, scrapbook__slug=scrapbook_slug)
        except Http404:
            return None

    def form_valid(self, form):
        self.object = self.get_object()
        if self.object is None:
            raise Http404("No Post matches the given query.")
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)

    def get_success_url(self):
        return reverse_lazy('scrapbook:scrapbook_detail', kwargs={'slug': self.object.scrapbook.slug})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'scrapbook/post_detail.html'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_slug = self.kwargs['post_slug']
        post = get_object_or_404(Post, slug=post_slug, scrapbook__slug=scrapbook_slug)
        if post.status != 2 and post.author != self.request.user:
            if not self.request.user.is_authenticated or not SharedAccess.objects.filter(user=self.request.user, scrapbook=post.scrapbook, post=post).exists():
                raise PermissionDenied("You do not have permission to view this post.")
        return post

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return HttpResponseForbidden("You do not have permission to view this post.")
    
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

@method_decorator(login_required, name='dispatch')
class ShareContentView(View):
    def get(self, request, *args, **kwargs):
        scrapbook_id = request.GET.get('scrapbook_id')
        scrapbook = get_object_or_404(Scrapbook, id=scrapbook_id)
        posts = Post.objects.filter(scrapbook=scrapbook).exclude(status=0)  # Exclude draft posts
        form = ShareContentForm(initial={'scrapbook_id': scrapbook.id}, shared_by=request.user, scrapbook=scrapbook)
        return render(request, 'scrapbook/share_content.html', {'form': form, 'object': scrapbook, 'posts': posts})

    def post(self, request, *args, **kwargs):
        scrapbook_id = request.GET.get('scrapbook_id')
        scrapbook = get_object_or_404(Scrapbook, id=scrapbook_id)
        form = ShareContentForm(request.POST, shared_by=request.user, scrapbook=scrapbook)
        if form.is_valid():
            shared_access = form.save(commit=False)
            shared_access.shared_by = request.user
            shared_access.save()
            messages.success(request, "Scrapbook and its posts shared successfully.")
            return redirect('scrapbook_detail', slug=scrapbook.slug)
        else:
            messages.error(request, "Failed to share the scrapbook.")
        posts = Post.objects.filter(scrapbook=scrapbook).exclude(status=0)  # Exclude draft posts
        return render(request, 'scrapbook/share_content.html', {'form': form, 'object': scrapbook, 'posts': posts})
    
class ScrapbookSharedDetailView(LoginRequiredMixin, generic.DetailView):
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_shareddetail.html'
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
        posts = scrapbook.posts.exclude(status=0)  # Exclude draft posts
        ordering = ["-created_on"]
        post_form = PostForm()
        
        # Pagination
        paginator = Paginator(posts, 6)  # Show 6 posts per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Get shared access for the current user and scrapbook
        sharedaccess = SharedAccess.objects.filter(user=self.request.user, scrapbook=scrapbook).exists()
        shared_posts = SharedAccess.objects.filter(user=self.request.user, scrapbook=scrapbook).values_list('post', flat=True)
        
        context.update({
            'posts': page_obj,
            'post_form': post_form,
            'is_paginated': page_obj.has_other_pages(),
            'page_obj': page_obj,
            'sharedaccess': sharedaccess,
            'shared_posts': shared_posts,
            'permission_denied': not sharedaccess and scrapbook.author != self.request.user and scrapbook.status != 2,
        })
        return context