from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
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
            'image': SimpleUploadedFile(name='test_image.jpg', content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b', content_type='image/jpeg'),
            'status': 1,
            'content': 'New Scrapbook Content',
            'description': 'New Scrapbook Description',
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful creation
        response = self.client.get(reverse('scrapbook:home'))
        self.assertContains(response, 'New Scrapbook')

    def test_scrapbook_update_view(self):
        # Test the ScrapbookUpdateView
        response = self.client.post(reverse('scrapbook:edit-scrapbook', kwargs={'slug': self.scrapbook.slug, 'scrapbook_id': self.scrapbook.id}), {
            'title': 'Updated Scrapbook',
            'image': SimpleUploadedFile(name='test_image.jpg', content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b', content_type='image/jpeg'),
            'status': 1,
            'content': 'Updated Scrapbook Content',
            'description': 'Updated Scrapbook Description',
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
            'image': SimpleUploadedFile(name='test_image.jpg', content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b', content_type='image/jpeg'),
            'status': 1,
            'content': 'New Post content',
        })
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
            'image': SimpleUploadedFile(name='test_image.jpg', content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b', content_type='image/jpeg'),
            'status': 2,
            'content': 'Updated Post content',
        })
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

    # Edge Test Skeletons
    def test_scrapbook_create_view_with_long_title(self):
        # Edge Test: Test the ScrapbookCreateView with a title that exceeds the maximum length
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:create-scrapbook'), {
            'title': 'a' * 101,
            'image': 'placeholder',
            'status': 1,
            'content': 'New Scrapbook Content',
            'description': 'New Scrapbook Description',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The title cannot be more than 100 characters.')

    def test_scrapbook_update_view_with_invalid_image_format(self):
        # Edge Test: Test the ScrapbookUpdateView with an invalid image format
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:edit-scrapbook', kwargs={'slug': self.scrapbook.slug, 'scrapbook_id': self.scrapbook.id}), {
            'title': 'Updated Scrapbook',
            'image': SimpleUploadedFile(name='test_image.gif', content=b'invalid_image', content_type='image/gif'),
            'status': 1,
            'content': 'Updated Scrapbook Content',
            'description': 'Updated Scrapbook Description',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.')

    def test_post_create_view_with_empty_content(self):
        # Edge Test: Test the PostCreateView with empty content
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:create-post', kwargs={'slug': self.scrapbook.slug}), {
            'scrapbook': self.scrapbook.id,
            'title': 'New Post',
            'image': 'placeholder',
            'status': 1,
            'content': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

    def test_post_update_view_with_special_characters_in_title(self):
        # Edge Test: Test the PostUpdateView with special characters in the title
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:edit-post', kwargs={'slug': self.scrapbook.slug, 'post_id': self.post.id}), {
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post! @#%^&*()_+{}:"<>?',
            'image': 'placeholder',
            'status': 1,
            'content': 'Updated Post content',
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Test Post! @#%^&*()_+{}:"<>?')

    def test_post_delete_view_non_existent_post(self):
        # Edge Test: Test the PostDeleteView with a non-existent post
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('scrapbook:delete-post', kwargs={'slug': self.scrapbook.slug, 'post_id': 999}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get(reverse('scrapbook:scrapbook_detail', kwargs={'slug': self.scrapbook.slug}))
        self.assertContains(response, 'Test Post')