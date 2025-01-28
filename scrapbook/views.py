from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.decorators.csrf import requires_csrf_token
from .models import Scrapbook, Post, SharedAccess
from .forms import PostForm, ScrapbookForm, ShareContentForm


class ScrapbookListView(generic.ListView):
    """
    View for displaying all public scrapbooks.

    Attributes:
    model -- The Scrapbook model.
    ordering -- The order in which the scrapbooks are displayed.
    template_name -- The template used to render the view.
    paginate_by -- The number of scrapbooks displayed per page.

    Methods:
    get_queryset -- Filter scrapbooks to only show public scrapbooks.
    get_context_data -- Add the number of posts in each scrapbook to the
    context.

    Template:
    scrapbook/index.html
    """
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
    """
    View for displaying the user's scrapbooks.

    Attributes:
    model -- The Scrapbook model.
    ordering -- The order in which the scrapbooks are displayed.
    template_name -- The template used to render the view.
    paginate_by -- The number of scrapbooks displayed per page.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    get_queryset -- Filter scrapbooks to only show the user's scrapbooks.
    get_context_data -- Add the number of posts in each scrapbook to the
    context.

    Template:
    scrapbook/scrapbook_mylist.html
    """
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_mylist.html"
    paginate_by = 6  # Show 6 scrapbooks per page
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the user's scrapbooks
        queryset = Scrapbook.objects.filter(
            author=self.request.user).order_by('-created_on')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context


class ScrapbookSharedListView(LoginRequiredMixin, generic.ListView):
    """
    View for displaying the user's shared scrapbooks.

    Attributes:
    model -- The Scrapbook model.
    ordering -- The order in which the scrapbooks are displayed.
    template_name -- The template used to render the view.
    paginate_by -- The number of scrapbooks displayed per page.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    get_queryset -- Filter scrapbooks to only show the shared scrapbooks.
    get_context_data -- Add the number of posts in each scrapbook to the
    context.

    Template:
    scrapbook/scrapbook_sharedlist.html
    """
    model = Scrapbook
    ordering = ["-created_on"]
    template_name = "scrapbook/scrapbook_sharedlist.html"
    paginate_by = 6  # Show 6 scrapbooks per page
    login_url = '/accounts/login/'

    def get_queryset(self):
        # Filter scrapbooks to only show the shared scrapbooks
        queryset = Scrapbook.objects.filter(
            sharedaccess__user=self.request.user).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(
            scrapbook__in=self.get_queryset(), status=2).count()
        return context


class ScrapbookDetailView(generic.DetailView):
    """
    View for displaying a scrapbook and its posts.

    Attributes:
    model -- The Scrapbook model.
    template_name -- The template used to render the view.

    Methods:
    get_object -- Get the scrapbook object.
    handle_no_permission -- Handle cases where the user does not have
    permission to view the scrapbook.
    get_context_data -- Add the posts in the scrapbook to the context.

    Template:
    scrapbook/scrapbook_detail.html
    """
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_detail.html'

    def get_object(self, queryset=None):
        scrapbook = super().get_object(queryset)
        user = self.request.user
        if (
            scrapbook.status != 2 and
            (not user.is_authenticated or scrapbook.author != user)
        ):
            if (
                not user.is_authenticated or
                not SharedAccess.objects.filter(
                    user=user,
                    scrapbook=scrapbook).exists()
            ):
                raise PermissionDenied(
                    "You do not have permission to view this scrapbook.")
        return scrapbook

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return HttpResponseForbidden(
            "You do not have permission to view this scrapbook.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scrapbook = self.get_object()
        posts = scrapbook.posts.all()
        paginator = Paginator(posts, 6)  # Show 6 posts per page

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ordering = ["-created_on"]

        # Get shared access for the current user and scrapbook
        sharedaccess = False
        if self.request.user.is_authenticated:
            sharedaccess = SharedAccess.objects.filter(
                user=self.request.user, scrapbook=scrapbook).exists()

        context.update({
            'scrapbook': scrapbook,
            'page_obj': page_obj,
            'posts': page_obj.object_list,
            'is_paginated': page_obj.has_other_pages(),
            'ordering': ordering,
            'sharedaccess': sharedaccess,
        })
        return context


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
    return redirect(reverse(
        'scrapbook:scrapbook_detail', kwargs={'slug': scrapbook.slug}))


class ScrapbookCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new scrapbook.

    Attributes:
    model -- The Scrapbook model.
    form_class -- The form used to create the scrapbook.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    form_valid -- Set the author of the scrapbook to the current user.
    get_success_url -- Redirect to the detail view of the created scrapbook.
    get_context_data -- Add the action to the context.

    Template:
    scrapbook/scrapbook_form.html
    """
    model = Scrapbook
    form_class = ScrapbookForm
    template_name = 'scrapbook/scrapbook_form.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Scrapbook created successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'scrapbook:scrapbook_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context


class ScrapbookUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a scrapbook.

    Attributes:
    model -- The Scrapbook model.
    form_class -- The form used to update the scrapbook.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    form_valid -- Display a success message when the form is valid.
    get_success_url -- Redirect to the user's scrapbook list.
    get_context_data -- Add the action to the context.

    Template:
    scrapbook/scrapbook_form.html
    """
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
    """
    View for deleting a scrapbook.

    Attributes:
    model -- The Scrapbook model.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    get_object -- Get the scrapbook object.
    form_valid -- Display a success message when the form is valid.
    get_success_url -- Redirect to the user's scrapbook list.

    Template:
    scrapbook/confirm_delete.html
    """
    model = Scrapbook
    template_name = 'scrapbook/confirm_delete.html'
    login_url = '/accounts/login/'

    def get_object(self):
        scrapbook_slug = self.kwargs['slug']
        scrapbook_id = self.kwargs['scrapbook_id']
        return get_object_or_404(
            Scrapbook, id=scrapbook_id, slug=scrapbook_slug)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Scrapbook deleted successfully.")
        return response

    def get_success_url(self):
        return reverse_lazy('my_scrapbook_list')


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new post.

    Attributes:
    model -- The Post model.
    form_class -- The form used to create the post.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    form_valid -- Set the author of the post to the current user.
    get_success_url -- Redirect to the detail view of the scrapbook.
    get_context_data -- Add the action and the scrapbook to the context.

    Template:
    scrapbook/post_form.html
    """
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    login_url = '/accounts/login/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['scrapbook'] = get_object_or_404(
            Scrapbook, slug=self.kwargs['scrapbook_slug'])
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
        context['scrapbook'] = get_object_or_404(
            Scrapbook, slug=self.kwargs['scrapbook_slug'])
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a post.

    Attributes:
    model -- The Post model.
    form_class -- The form used to update the post.
    template_name -- The template used to render the view.

    Methods:
    get_object -- Get the post object.
    form_valid -- Display a success message when the form is valid.
    get_success_url -- Redirect to the detail view of the scrapbook.
    get_context_data -- Add the action and the scrapbook to the context.

    Template:
    scrapbook/post_form.html
    """
    model = Post
    form_class = PostForm
    template_name = 'scrapbook/post_form.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_id = self.kwargs['post_id']
        return get_object_or_404(
            Post, id=post_id, scrapbook__slug=scrapbook_slug)

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
        context['scrapbook'] = get_object_or_404(
            Scrapbook, slug=self.kwargs['scrapbook_slug'])
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a post.

    Attributes:
    model -- The Post model.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    get_object -- Get the post object.
    form_valid -- Display a success message when the form is valid.
    get_success_url -- Redirect to the detail view of the scrapbook.

    Template:
    scrapbook/confirm_delete.html
    """
    model = Post
    template_name = 'scrapbook/confirm_delete.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_id = self.kwargs['post_id']
        try:
            return get_object_or_404(
                Post, id=post_id, scrapbook__slug=scrapbook_slug)
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
        return reverse_lazy(
            'scrapbook:scrapbook_detail', kwargs={
                'slug': self.object.scrapbook.slug})


class PostDetailView(generic.DetailView):
    """
    View for displaying a post.

    Attributes:
    model -- The Post model.
    template_name -- The template used to render the view.

    Methods:
    get_object -- Get the post object.
    handle_no_permission -- Handle cases where the user does not have
    permission to view the post.

    Template:
    scrapbook/post_detail.html
    """
    model = Post
    template_name = 'scrapbook/post_detail.html'

    def get_object(self, queryset=None):
        scrapbook_slug = self.kwargs['scrapbook_slug']
        post_slug = self.kwargs['post_slug']
        post = get_object_or_404(
            Post, slug=post_slug, scrapbook__slug=scrapbook_slug)
        user = self.request.user
        if post.status != 2 and post.author != user:
            if (
                not user.is_authenticated or
                not SharedAccess.objects.filter(
                    user=user, scrapbook=post.scrapbook
                ).exists()
            ):
                raise PermissionDenied(
                    "You do not have permission to view this post."
                )
        return post

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return HttpResponseForbidden(
            "You do not have permission to view this post.")

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
    """
    View for sharing a scrapbook and its posts with another user.

    Attributes:
    template_name -- The template used to render the view.

    Methods:
    get -- Display the form for sharing the scrapbook.
    post -- Share the scrapbook and its posts with the user.

    Template:
    scrapbook/share_content.html
    """
    def get(self, request, *args, **kwargs):
        scrapbook_id = request.GET.get('scrapbook_id')
        scrapbook = get_object_or_404(Scrapbook, id=scrapbook_id)
        posts = Post.objects.filter(
            scrapbook=scrapbook).exclude(status=0)  # Exclude draft posts
        form = ShareContentForm(initial={
            'scrapbook_id': scrapbook.id},
            shared_by=request.user, scrapbook=scrapbook)
        return render(
            request, 'scrapbook/share_content.html', {
                'form': form, 'object': scrapbook, 'posts': posts})

    def post(self, request, *args, **kwargs):
        scrapbook_id = request.GET.get('scrapbook_id')
        scrapbook = get_object_or_404(Scrapbook, id=scrapbook_id)
        form = ShareContentForm(
            request.POST,
            shared_by=request.user,
            scrapbook=scrapbook)
        if form.is_valid():
            shared_access = form.save(commit=False)
            shared_access.shared_by = request.user
            shared_access.save()
            messages.success(
                request, "Scrapbook and its posts shared successfully.")
            return redirect('scrapbook_detail', slug=scrapbook.slug)
        else:
            messages.error(request, "Failed to share the scrapbook.")
        posts = Post.objects.filter(
            scrapbook=scrapbook).exclude(status=0)  # Exclude draft posts
        return render(
            request, 'scrapbook/share_content.html', {
                'form': form,
                'object': scrapbook,
                'posts': posts})


class ScrapbookSharedDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View for displaying a shared scrapbook and its posts.

    Attributes:
    model -- The Scrapbook model.
    template_name -- The template used to render the view.
    login_url -- The URL to redirect to if the user is not logged in.

    Methods:
    get_object -- Get the scrapbook object.
    handle_no_permission -- Handle cases where the user does not have
    permission to view the scrapbook.
    get_context_data -- Add the posts in the scrapbook to the context.

    Template:
    scrapbook/scrapbook_shareddetail.html
    """
    model = Scrapbook
    template_name = 'scrapbook/scrapbook_shareddetail.html'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        scrapbook = super().get_object(queryset)
        if scrapbook.status != 2 and scrapbook.author != self.request.user:
            if not SharedAccess.objects.filter(
                user=self.request.user, scrapbook=scrapbook
            ).exists():
                raise PermissionDenied(
                    "You do not have permission to view this scrapbook."
                )
        return scrapbook

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return HttpResponseForbidden(
            "You do not have permission to view this scrapbook.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scrapbook = self.get_object()
        posts = scrapbook.posts.exclude(status=0)  # Exclude draft posts
        paginator = Paginator(posts, 6)  # Show 6 posts per page

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ordering = ["-created_on"]

        # Get shared access for the current user and scrapbook
        sharedaccess = SharedAccess.objects.filter(
            user=self.request.user, scrapbook=scrapbook).exists()

        # Get shared posts for the current user and scrapbook
        shared_posts = SharedAccess.objects.filter(
            user=self.request.user,
            scrapbook=scrapbook).values_list('post', flat=True)

        context.update({
            'scrapbook': scrapbook,
            'page_obj': page_obj,
            'posts': page_obj.object_list,
            'is_paginated': page_obj.has_other_pages(),
            'ordering': ordering,
            'sharedaccess': sharedaccess,
            'shared_posts': shared_posts,
        })
        return context


def custom_permission_denied_view(request, exception):
    # Return a custom 403 error page
    return render(request, '403.html', status=403)


def custom_page_not_found_view(request, exception):
    # Return a custom 404 error page
    return render(request, '404.html', status=404)


def custom_error_view(request):
    # Return a custom 500 error page
    return render(request, '500.html', status=500)


def custom_bad_request_view(request, exception):
    # Return a custom 400 error page
    return render(request, '400.html', status=400)


def trigger_500_error(request):
    # Intentionally raise an exception to trigger a 500 error
    raise Exception("Intentional 500 error for testing purposes")


def trigger_403_error(request):
    # Intentionally raise a PermissionDenied exception to trigger a 403 error
    raise PermissionDenied("Intentional 403 error for testing purposes")
