from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PostForm
from .models import Scrapbook, Post
from django.contrib.auth.models import User

class PostFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)

    def test_post_form_valid_data(self):
        # Test the PostForm with valid data
        pass
        # image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        # image = SimpleUploadedFile(name='test_image.jpg', content=image_content, content_type='image/jpeg')
        # form = PostForm(data={
        #     'title': 'Test Post',
        #     'content': 'Test Post Content',
        #     'status': 1,
        # }, files={'image': image})
        # if not form.is_valid():
        #     print(form.errors)
        # self.assertTrue(form.is_valid())
        # post = form.save(commit=False)
        # post.author = self.user
        # post.scrapbook = self.scrapbook
        # post.save()
        # self.assertEqual(post.title, 'Test Post')
        # self.assertEqual(post.content, 'Test Post Content')
        # self.assertEqual(post.status, 1)
        # self.assertTrue(post.image.public_id.startswith('test_image'))

    def test_post_form_invalid_data(self):
        # Test the PostForm with invalid data
        pass
        # self.user = User.objects.create_user(username='testuser', password='testpass')
        # self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        # image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        # image = SimpleUploadedFile(name='test_image.jpg', content=image_content, content_type='image/jpeg')
        # form = PostForm(data={
        #     'title': 'Test Post',
        #     'content': 'Test Post Content',
        #     'status': 1,
        # }, files={'image': image})
        # if not form.is_valid():
        #     print(form.errors)
        # self.assertTrue(form.is_valid())
        # post = form.save(commit=False)
        # post.author = self.user
        # post.scrapbook = self.scrapbook
        # post.save()
        # self.assertEqual(post.title, 'Test Post')
        # self.assertEqual(post.content, 'Test Post Content')
        # self.assertEqual(post.status, 1)
        # self.assertTrue(post.image.public_id.startswith('test_image'))


    def test_post_form_missing_title(self):
        # Test the PostForm with missing title
        pass

    def test_post_form_missing_content(self):
        # Test the PostForm with missing content
        pass

    def test_post_form_missing_status(self):
        # Test the PostForm with missing status
        pass

    def test_post_form_missing_image(self):
        # Test the PostForm with missing image
        pass

    def test_post_form_invalid_image_format(self):
        # Test the PostForm with an invalid image format
        pass

    def test_post_form_valid_image_format(self):
        # Test the PostForm with a valid image format
        pass