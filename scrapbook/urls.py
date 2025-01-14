from . import views
from django.urls import path

urlpatterns = [
    path("", views.ScrapbookListView.as_view(), name="home"),
    path('<slug:slug>/', views.scrapbook_detail, name='scrapbook_detail'),
    path('<slug:slug>/edit_post/<int:post_id>',
         views.post_edit, name='post_edit'),
]