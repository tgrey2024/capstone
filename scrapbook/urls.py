from . import views
from django.urls import path

urlpatterns = [
    path("", views.ScrapbookListView.as_view(), name="home"),
    path('<slug:slug>/', views.scrapbook_detail, name='scrapbook_detail'),
    path('<slug:slug>/create/', views.PostCreateView.as_view(), name="create-post"),
    path('<slug:slug>/edit/<int:post_id>', views.PostUpdateView.as_view(), name="edit-post"),
    path('<slug:slug>/delete/<int:post_id>', views.PostDeleteView.as_view(), name="delete-post"),
]