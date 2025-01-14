from . import views
from django.urls import path

urlpatterns = [
    path("", views.ScrapbookListView.as_view(), name="home"),
    path('<slug:slug>/', views.scrapbook_detail, name='scrapbook_detail'),
]