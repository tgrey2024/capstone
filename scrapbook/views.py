from django.shortcuts import render
from django.views import generic
from .models import Scrapbook

# Create your views here.
class ScrapbookListView(generic.ListView):
    queryset = Scrapbook.objects.all()
    template_name = "scrapbook/index.html"
    # context_object_name = "scrapbooks"
    paginate_by = 3


