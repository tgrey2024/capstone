from django.shortcuts import render
from django.views import generic
from .models import Scrapbook

# Create your views here.
class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.filter(status=2).order_by("-created_on")
    template_name = "scrapbook/index.html"
    # context_object_name = "scrapbooks"
    paginate_by = 3


