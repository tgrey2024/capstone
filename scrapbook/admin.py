from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Scrapbook, Post, SharedAccess


@admin.register(Scrapbook)
class ScrapbookAdmin(SummernoteModelAdmin):
    """
    Admin class for the Scrapbook model.

    This class is used to customize the admin interface for the Scrapbook
    model.
    """
    list_display = ('title', 'slug', 'status', 'author')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for the Post model.

    This class is used to customize the admin interface for the Post model.

    """

    list_display = ('title', 'slug', 'status', 'author', 'scrapbook')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(SharedAccess)
class SharedAccessAdmin(admin.ModelAdmin):
    """
    Admin class for the SharedAccess model.

    This class is used to customize the admin interface for the SharedAccess
    model.

    """

    list_display = ('user', 'scrapbook', 'shared_by')
    search_fields = ['scrapbook__title', 'user__username']
    list_filter = ('scrapbook', 'user', 'shared_by')
