from django.urls import path
from . import views

handler403 = 'scrapbook.views.custom_permission_denied_view'

urlpatterns = [
    path('trigger-403-error/', views.trigger_403_error, name='trigger-403-error'),
    path('trigger-500-error/', views.trigger_500_error, name='trigger-500-error'),
    path("", views.ScrapbookListView.as_view(), name="home"),
    path("my-scrapbooks/", views.ScrapbookMyListView.as_view(), name="my_scrapbook_list"),
    path("shared-scrapbooks/", views.ScrapbookSharedListView.as_view(), name="shared_scrapbook_list"),
    path('share/', views.ShareContentView.as_view(), name='share_content'),
    path('create-scrapbook/', views.ScrapbookCreateView.as_view(), name="create-scrapbook"),
    path('<slug:slug>/', views.ScrapbookDetailView.as_view(), name='scrapbook_detail'),
    path('shared/<slug:slug>/', views.ScrapbookSharedDetailView.as_view(), name='shared_scrapbook_detail'),
    path('<slug:slug>/edit-scrapbook/<int:scrapbook_id>/', views.ScrapbookUpdateView.as_view(), name='edit-scrapbook'),
    path('<slug:slug>/delete-scrapbook/<int:scrapbook_id>/', views.ScrapbookDeleteView.as_view(), name="delete-scrapbook"),
    path('<slug:scrapbook_slug>/create-post/', views.PostCreateView.as_view(), name='create-post'),
    path('<slug:scrapbook_slug>/edit-post/<int:post_id>/', views.PostUpdateView.as_view(), name='edit-post'),
    path('<slug:scrapbook_slug>/delete-post/<int:post_id>/', views.PostDeleteView.as_view(), name='delete-post'),
    path('<slug:scrapbook_slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
]