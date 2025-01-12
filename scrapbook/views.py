from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Scrapbook, Post, Image

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
        # content["images"] = self.get_object().posts.image.all()
        return context