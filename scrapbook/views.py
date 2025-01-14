from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.db import transaction
from .models import Scrapbook, Post, Image
from .forms import PostForm

class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.filter(status=2).order_by("-created_on")
    template_name = "scrapbook/index.html"
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = Post.objects.filter(scrapbook__in=self.queryset, status=2).count()
        return context
    
def scrapbook_detail(request, slug):
    scrapbook = get_object_or_404(Scrapbook, slug=slug)
    posts = scrapbook.posts.filter(status=2).order_by("created_on")
    post_form = PostForm()

    if request.method == 'POST':
        return handle_post_request(request, scrapbook)

    context = {
        'scrapbook': scrapbook,
        'posts': posts,
        'post_form': post_form,
    }
    return render(request, 'scrapbook/scrapbook_detail.html', context)

@transaction.atomic
def handle_post_request(request, scrapbook):
    post_form = PostForm(data=request.POST, files=request.FILES)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.author = request.user
        post.scrapbook = scrapbook
        post.save()
        if 'image' in request.FILES:
            Image.objects.create(post=post, featured_image=request.FILES['image'])
        elif 'image_url' in request.POST:
            Image.objects.create(post=post, featured_image=request.POST['image_url'])
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': post_form.errors})

def post_edit(request, slug, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post_form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': post_form.errors})
    else:
        post_form = PostForm(instance=post)
    return render(request, 'scrapbook/post_edit.html', {'post_form': post_form, 'scrapbook': post.scrapbook})