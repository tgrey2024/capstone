from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Scrapbook, Post, Image
from .forms import PostForm

# Create your views here.
class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.filter(status=2).order_by("-created_on")
    template_name = "scrapbook/index.html"
    # context_object_name = "scrapbooks"
    paginate_by = 3


class ScrapbookDetailView(generic.DetailView):
    model = Scrapbook
    template_name = "scrapbook/scrapbook_detail.html"
    context_object_name = "scrapbook"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = self.get_object().posts.filter(status=2).order_by("-created_on")
        context["post_form"] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.scrapbook = self.object
            post.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Post added successfully'
    )
            return redirect('scrapbook_detail', slug=self.object.slug)
        context["post_form"] = post_form
        return self.render_to_response(context)

