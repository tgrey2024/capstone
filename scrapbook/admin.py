from django.contrib import admin
from .models import Scrapbook, Post, SharedAccess
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.
@admin.register(Scrapbook)
class ScrapbookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'author')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'author', 'scrapbook')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(SharedAccess)
class SharedAccessAdmin(admin.ModelAdmin):

    list_display = ('user', 'scrapbook', 'shared_by')
    search_fields = ['scrapbook__title', 'user__username']
    list_filter = ('scrapbook', 'user')