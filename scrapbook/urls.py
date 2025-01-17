from . import views
from django.urls import path

urlpatterns = [
    path("", views.ScrapbookListView.as_view(), name="home"),
    path('create-scrapbook/', views.ScrapbookCreateView.as_view(), name="create-scrapbook"),
    path('<slug:slug>/', views.scrapbook_detail, name='scrapbook_detail'),
    path('<slug:slug>/edit-scrapbook/<int:scrapbook_id>', views.ScrapbookUpdateView.as_view(), name="edit-scrapbook"),
    path('<slug:slug>/delete-scrapbook/<int:scrapbook_id>', views.ScrapbookDeleteView.as_view(), name="delete-scrapbook"),
    path('<slug:slug>/create-post/', views.PostCreateView.as_view(), name="create-post"),
    path('<slug:scrapbook_slug>/post/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit-post/<int:post_id>', views.PostUpdateView.as_view(), name="edit-post"),
    path('<slug:slug>/delete-post/<int:post_id>', views.PostDeleteView.as_view(), name="delete-post"),
]