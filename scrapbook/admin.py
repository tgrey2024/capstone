from django.contrib import admin
from .models import Scrapbook, Post, Image

# Register your models here.
admin.site.register(Scrapbook)

admin.site.register(Post)

admin.site.register(Image)