from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse
from django.db import transaction
from .models import Scrapbook, Post, Image
from .forms import PostForm

class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.filter(status=2).order_by("-created_on")
    template_name = "scrapbook/index.html"
    # context_object_name = "scrapbooks"
    paginate_by = 3
    
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
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': post_form.errors})