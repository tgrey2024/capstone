from django.contrib import admin
from .models import Scrapbook, Post, Image
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
@admin.register(Scrapbook)
class ScrapbookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    
admin.site.register(Image)