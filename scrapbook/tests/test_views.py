from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from scrapbook.models import Scrapbook, Post, SharedAccess
from scrapbook.forms import ShareContentForm


class ScrapbookViewsTest(TestCase):
    """
    Tests for the views in the scrapbook app.

    The ScrapbookViewsTest class contains tests for the views in the
    scrapbook app.
    The setUp method creates a client, users, scrapbooks, and posts for
    testing.

    """
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1', password='testpass')
        self.user2 = User.objects.create_user(
            username='user2', password='testpass')
        self.scrapbook1 = Scrapbook.objects.create(
            title='Scrapbook 1', author=self.user1, status=1)
        self.scrapbook2 = Scrapbook.objects.create(
            title='Scrapbook 2', author=self.user2, status=1)
        self.scrapbook = Scrapbook.objects.create(
            title='Test Scrapbook', author=self.user1, status=2)
        self.post = Post.objects.create(
            title='Test Post', author=self.user1,
            scrapbook=self.scrapbook, status=1)
        self.client.login(username='user1', password='testpass')
        self.scrapbook.save()
        self.post.save()
        self.user1.save()

    def test_scrapbook_list_view(self):
        # Test the ScrapbookListView
        response = self.client.get(reverse('scrapbook:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Scrapbook')

    def test_scrapbook_detail_view(self):
        # Test the ScrapbookDetailView
        response = self.client.get(reverse(
            'scrapbook:scrapbook_detail',
            kwargs={'slug': self.scrapbook.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_detail.html')
        self.assertContains(response, 'Test Scrapbook')
        self.assertContains(response, 'user1')

    def test_scrapbook_create_view(self):
        # Test the ScrapbookCreateView
        self.client.login(username='user1', password='testpass')
        content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=content,
            content_type='image/jpeg'
        )
        response = self.client.post(reverse('scrapbook:create-scrapbook'), {
            'title': 'New Scrapbook',
            'image': image,
            'status': 1,
            'content': 'New Scrapbook Content',
            'description': 'New Scrapbook Description',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('scrapbook:home'))
        self.assertContains(response, 'New Scrapbook')

    def test_scrapbook_update_view(self):
        # Test the ScrapbookUpdateView
        content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=content,
            content_type='image/jpeg'
        )
        response = self.client.post(reverse(
            'scrapbook:edit-scrapbook', kwargs={
                'slug': self.scrapbook.slug,
                'scrapbook_id': self.scrapbook.id}), {
            'title': 'Updated Scrapbook',
            'image': image,
            'status': 1,
            'content': 'Updated Scrapbook Content',
            'description': 'Updated Scrapbook Description',
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(
            reverse('scrapbook:scrapbook_detail', kwargs={
                'slug': self.scrapbook.slug}))
        self.assertContains(response, 'Updated Scrapbook')

    def test_scrapbook_delete_view(self):
        # Test the ScrapbookDeleteView
        response = self.client.post(
            reverse('scrapbook:delete-scrapbook', kwargs={
                'slug': self.scrapbook.slug,
                'scrapbook_id': self.scrapbook.id}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('scrapbook:home'))
        self.assertNotContains(response, 'Test Scrapbook')

    # Edge Tests
    def test_scrapbook_create_view_with_long_title(self):
        # Edge Test: Test the ScrapbookCreateView with a title that
        # exceeds the maximum length
        self.client.login(username='user1', password='testpass')
        response = self.client.post(reverse('scrapbook:create-scrapbook'), {
            'title': 'a' * 101,
            'image': 'placeholder',
            'status': 1,
            'content': 'New Scrapbook Content',
            'description': 'New Scrapbook Description',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'The title cannot be more than 100 characters.')

    def test_scrapbook_update_view_with_invalid_image_format(self):
        # Edge Test: Test the ScrapbookUpdateView with an invalid image format
        self.client.login(username='user1', password='testpass')
        response = self.client.post(
            reverse('scrapbook:edit-scrapbook', kwargs={
                'slug': self.scrapbook.slug,
                'scrapbook_id': self.scrapbook.id}), {
                'title': 'Updated Scrapbook',
                'image': SimpleUploadedFile(
                    name='test_image.gif', content=b'invalid_image',
                    content_type='image/gif'),
                'status': 1,
                'content': 'Updated Scrapbook Content',
                'description': 'Updated Scrapbook Description',
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'Upload a valid image or an uncorrupted image.')

    def test_post_detail_view(self):
        # Test the PostDetailView
        response = self.client.get(
            reverse('scrapbook:post_detail', kwargs={
                'scrapbook_slug': self.scrapbook.slug,
                'post_slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_post_create_view(self):
        # Test the PostCreateView
        content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=content,
            content_type='image/jpeg'
        )
        response = self.client.post(
            reverse('create-post', kwargs={
                'scrapbook_slug': self.scrapbook.slug}), {
                'scrapbook': self.scrapbook.id,
                'title': 'New Post',
                'image': image,
                'status': 1,
                'content': 'New Post content',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_update_view(self):
        # Test the PostUpdateView
        self.client.login(username='user1', password='testpass')
        content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=content,
            content_type='image/jpeg'
        )
        response = self.client.post(
            reverse('edit-post', kwargs={
                'scrapbook_slug': self.scrapbook.slug,
                'post_id': self.post.id}), {
                'scrapbook': self.scrapbook.id,
                'title': 'Updated Post',
                'image': image,
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
        self.client.login(username='user1', password='testpass')
        response = self.client.post(
            reverse('delete-post', kwargs={
                'scrapbook_slug': self.scrapbook.slug,
                'post_id': self.post.id
            }))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.get(
            reverse('scrapbook:scrapbook_detail', kwargs={
                'slug': self.scrapbook.slug}))
        self.assertNotContains(response, 'Test Post')

    # Edge Tests
    def test_post_update_view_with_special_characters_in_title(self):
        # Edge Test: Test the PostUpdateView with special characters
        # in the title
        response = self.client.post(
            reverse('edit-post', kwargs={
                'scrapbook_slug': self.scrapbook.slug,
                'post_id': self.post.id}), {
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
        self.client.login(username='user1', password='testpass')
        response = self.client.post(
            reverse('delete-post', kwargs={
                'scrapbook_slug': self.scrapbook.slug, 'post_id': 999}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get(
            reverse('scrapbook:scrapbook_detail', kwargs={
                'slug': self.scrapbook.slug}))
        self.assertContains(response, 'Test Post')

    def test_user_without_permission_cannot_access_scrapbook(self):
        # Test that a user without permission cannot access a private scrapbook
        self.client.login(username='user1', password='testpass')
        response = self.client.get(
            reverse('scrapbook_detail', kwargs={'slug': self.scrapbook2.slug})
        )
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')
        self.assertContains(
            response,
            'You do not have permission to view this scrapbook.',
            status_code=403)

    def test_user_with_permission_can_access_scrapbook(self):
        # Test that a user with permission can access a shared scrapbook
        SharedAccess.objects.create(
            user=self.user1, scrapbook=self.scrapbook2, shared_by=self.user2)
        self.client.login(username='user1', password='testpass')
        response = self.client.get(
            reverse('scrapbook_detail', kwargs={'slug': self.scrapbook2.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_detail.html')
        self.assertContains(response, 'Scrapbook 2')


class ScrapbookMyListViewTest(TestCase):
    """
    Tests for the ScrapbookMyListView view.

    The ScrapbookMyListViewTest class contains tests for the
    ScrapbookMyListView view.
    The setUp method creates a client, users, scrapbooks and posts for testing.
    """
    def setUp(self):
        # Create a client for testing
        self.client = Client()
        # Create users for testing
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass'
            )
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass')
        # Create scrapbooks for testing
        self.scrapbook1 = Scrapbook.objects.create(
            title='Scrapbook 1',
            author=self.user1,
            status=1)
        self.scrapbook2 = Scrapbook.objects.create(
            title='Scrapbook 2',
            author=self.user2,
            status=1)
        # Create posts for testing
        self.post1 = Post.objects.create(
            title='Post 1',
            status=1,
            author=self.user1,
            scrapbook=self.scrapbook1)
        self.post2 = Post.objects.create(
            title='Post 2',
            status=1,
            author=self.user2,
            scrapbook=self.scrapbook2)
        # Share scrapbook2 with user1
        SharedAccess.objects.create(
            user=self.user1,
            scrapbook=self.scrapbook2,
            shared_by=self.user2)
        posts = Post.objects.filter(scrapbook=self.scrapbook2)
        for post in posts:
            SharedAccess.objects.create(
                user=self.user1,
                scrapbook=self.scrapbook2,
                post=post,
                shared_by=self.user2)

    def test_my_scrapbooks_view(self):
        # Test the view for the user's own scrapbooks
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('my_scrapbook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_mylist.html')
        # Check that 'Scrapbook 1' is in the #my-scrapbooks section
        self.assertContains(response, 'Scrapbook 1')
        self.assertNotContains(response, 'Scrapbook 2')

    def test_shared_scrapbooks_view(self):
        # Test the view for scrapbooks shared with the user
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('shared_scrapbook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'scrapbook/scrapbook_sharedlist.html')
        # Check that 'Scrapbook 2' is in the #shared-scrapbooks section
        self.assertContains(response, 'Scrapbook 2')
        self.assertNotContains(response, 'Scrapbook 1')

    def test_shared_scrapbooks_not_in_my_scrapbooks(self):
        # Test that shared scrapbooks do not appear in the
        # user's own scrapbooks list
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('my_scrapbook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_mylist.html')
        # Check that 'Scrapbook 2' is not in the #my-scrapbooks section
        self.assertNotContains(response, 'Scrapbook 2')

    def test_my_scrapbooks_not_in_shared_scrapbooks(self):
        # Test that the user's own scrapbooks do not appear
        # in the shared scrapbooks list
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('shared_scrapbook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'scrapbook/scrapbook_sharedlist.html')
        # Check that 'Scrapbook 1' is not in the #shared-scrapbooks section
        self.assertNotContains(response, 'Scrapbook 1')

    def test_shared_scrapbooks_access(self):
        # Test that the user can access shared scrapbooks
        self.client.login(username='user1', password='testpass')
        response = self.client.get(
            reverse('scrapbook_detail', kwargs={'slug': self.scrapbook2.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_detail.html')
        self.assertContains(response, 'Scrapbook 2')

    def test_shared_scrapbooks_access_posts(self):
        # Test that the user can access shared posts
        self.client.login(username='user1', password='testpass')
        response = self.client.get(
            reverse(
                'post_detail',
                kwargs={
                    'scrapbook_slug': self.scrapbook2.slug,
                    'post_slug': self.post2.slug
                }
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/post_detail.html')
        self.assertContains(response, 'Post 2')

    def test_shared_scrapbooks_access_posts_not_in_my_scrapbooks(self):
        # Test that shared posts do not appear in the user's own scrapbooks
        # list
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('my_scrapbook_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/scrapbook_mylist.html')
        # Check that 'Post 2' is not in the #my-scrapbooks section
        self.assertNotContains(response, 'Post 2')


class ShareContentViewTest(TestCase):
    """
    Test case for the ShareContentView.

    This test case includes tests for the ShareContentView to ensure that
    the view behaves as expected when sharing a scrapbook or post with
    another user.
    """

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1', password='testpass')
        self.user2 = User.objects.create_user(
            username='user2', password='testpass')
        self.scrapbook = Scrapbook.objects.create(
            title='Test Scrapbook', author=self.user1)
        self.post1 = Post.objects.create(
            title='Test Post 1', author=self.user1, scrapbook=self.scrapbook,
            status=1)
        self.post2 = Post.objects.create(
            title='Test Post 2', author=self.user1, scrapbook=self.scrapbook,
            status=1)

    def test_share_scrapbook_with_invalid_user(self):
        # Test sharing a scrapbook with an invalid user
        self.client.login(username='user1', password='testpass')
        response = self.client.post(reverse(
            'share_content') + f'?scrapbook_id={self.scrapbook.id}', {
            'user': 999,
            'scrapbook_id': self.scrapbook.id,
            'post_id': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Select a valid choice.")

    def test_share_scrapbook_without_login(self):
        # Test sharing a scrapbook without logging in
        response = self.client.post(reverse(
            'share_content') + f'?scrapbook_id={self.scrapbook.id}', {
            'user': self.user2.id,
            'scrapbook_id': self.scrapbook.id,
            'post_id': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/accounts/login/?next=' + reverse(
                'share_content') + f'?scrapbook_id={self.scrapbook.id}')

    def test_get_share_content_view(self):
        # Test the GET request for the ShareContentView
        self.client.login(username='user1', password='testpass')
        response = self.client.get(
            reverse('share_content') + f'?scrapbook_id={self.scrapbook.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scrapbook/share_content.html')
        self.assertContains(response, 'Share Content')

    def test_post_share_content_view_invalid_data(self):
        # Test the POST request for the ShareContentView with invalid data
        self.client.login(username='user1', password='testpass')
        response = self.client.post(
            reverse('share_content') + f'?scrapbook_id={self.scrapbook.id}', {
                'user': '',
                'scrapbook_id': self.scrapbook.id,
                'post_id': ''
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
