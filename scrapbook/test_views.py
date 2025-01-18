from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Scrapbook, Post

class ScrapbookViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.post = Post.objects.create(title='Test Post', author=self.user, scrapbook=self.scrapbook, status=1)
        self.client.login(username='testuser', password='testpass')
        self.scrapbook.save()
        self.post.save()
        self.user.save()


    def test_scrapbook_list_view(self):
        # Test the ScrapbookListView
        response = self.client.get(reverse('scrapbook:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/index.html')
        self.assertContains(response, 'Test Scrapbook')
        self.assertContains(response, 'by testuser')


    def test_scrapbook_detail_view(self):
        # Test the ScrapbookDetailView
        response = self.client.get(reverse('scrapbook:scrapbook_detail', kwargs={'slug': self.scrapbook.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_detail.html')
        self.assertContains(response, 'Test Scrapbook')
        self.assertContains(response, 'testuser')

    def test_scrapbook_create_view(self):
        # Test the ScrapbookCreateView
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:create-scrapbook'), {
            'title': 'New Scrapbook',
            'image': 'placeholder',
            'status': 1,
            'content': 'New Scrapbook Content',
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful creation
        response = self.client.get(reverse('scrapbook:home'))
        self.assertContains(response, 'New Scrapbook')

    def test_scrapbook_update_view(self):
        # Test the ScrapbookUpdateView
        response = self.client.post(reverse('scrapbook:edit-scrapbook', kwargs={'slug': self.scrapbook.slug, 'scrapbook_id': self.scrapbook.id}), {
            'title': 'Updated Scrapbook',
            'image': 'placeholder',
            'status': 1,
            'content': 'Updated Scrapbook Content',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('scrapbook:scrapbook_detail', kwargs={'slug': self.scrapbook.slug}))
        self.assertContains(response, 'Updated Scrapbook')


    def test_scrapbook_delete_view(self):
        # Test the ScrapbookDeleteView
        response = self.client.post(reverse('scrapbook:delete-scrapbook', kwargs={'slug': self.scrapbook.slug, 'scrapbook_id': self.scrapbook.id}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('scrapbook:home'))
        self.assertNotContains(response, 'Test Scrapbook')

    def test_post_detail_view(self):
        # Test the PostDetailView
        response = self.client.get(reverse('scrapbook:post_detail', kwargs={'scrapbook_slug': self.scrapbook.slug, 'post_slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/post_detail.html')
        self.assertContains(response, 'Test Post')


    def test_post_create_view(self):
        # Test the PostCreateView
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:create-post', kwargs={'slug': self.scrapbook.slug}), {
            'scrapbook': self.scrapbook.id,
            'title': 'New Post',
            'image': 'placeholder',
            'status': 1,
            'content': 'New Post content',
        })
        if response.status_code != 302:
            print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)
        new_post = Post.objects.get(title='New Post')
        self.assertEqual(new_post.author, self.user)
        self.assertEqual(new_post.scrapbook, self.scrapbook)
        self.assertEqual(new_post.status, 1)
        self.assertEqual(new_post.content, 'New Post content')

    def test_post_update_view(self):
        # Test the PostUpdateView
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:edit-post', kwargs={'slug': self.scrapbook.slug, 'post_id': self.post.id}), {
            'scrapbook': self.scrapbook.id,
            'title': 'Updated Post',
            'image': 'placeholder',
            'status': 2,
            'content': 'Updated Post content',
        })
        if response.status_code != 302:
            print(response.content)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.status, 2)
        self.assertEqual(self.post.content, 'Updated Post content')
    

    def test_post_delete_view(self):
        # Test the PostDeleteView
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:delete-post', kwargs={'slug': self.scrapbook.slug, 'post_id': self.post.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.get(reverse('scrapbook:scrapbook_detail', kwargs={'slug': self.scrapbook.slug}))
        self.assertNotContains(response, 'Test Post')
        