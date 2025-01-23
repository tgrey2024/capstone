from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PostForm, ShareContentForm
from .models import Scrapbook, Post, SharedAccess
from django.contrib.auth.models import User
from PIL import Image
from PIL import ImageFile
from PIL.Image import DecompressionBombWarning
import io
import warnings

# Suppress DecompressionBombWarning
warnings.simplefilter('ignore', DecompressionBombWarning)
ImageFile.LOAD_TRUNCATED_IMAGES = True

class PostFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)

    def test_post_form_valid_data(self):
        # Test the PostForm with valid data
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        image = SimpleUploadedFile(name='test_image.jpg', content=image_content, content_type='image/jpeg')
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post',
            'content': 'Test Post Content',
            'status': 1,
        }, files={'image': image})
        self.assertTrue(form.is_valid())
        post = form.save(commit=False)
        post.author = self.user
        post.scrapbook = self.scrapbook
        post.save()
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Post Content')
        self.assertEqual(post.status, 1)
        self.assertTrue(post.image is not None)
        self.assertTrue(post.image != '')

    def test_post_form_invalid_data(self):
        # Test the PostForm with invalid data
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_post_form_missing_title(self):
        # Test the PostForm with missing title
        form = PostForm(data={'content': 'Test Post Content', 'status': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_post_form_max_length_title(self):
        # Edge Test: Test the PostForm with maximum length title
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'a' * 100,
            'content': 'Test Post Content',
            'status': 1,
        })
        self.assertTrue(form.is_valid())

    def test_post_form_exceed_length_title(self):
        # Edge Test: Test the PostForm with exceeding length title
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'a' * 101,
            'content': 'Test Post Content',
            'status': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], [
            "The title cannot be more than 100 characters."])

    def test_post_form_special_characters(self):
        # Edge Test: Test the PostForm with special characters in title and content
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post! @#%^&*()_+{}:"<>?',
            'content': 'Test Post Content! @#%^&*()_+{}:"<>?',
            'status': 1,
        })
        self.assertTrue(form.is_valid())
        post = form.save(commit=False)
        post.author = self.user
        post.scrapbook = self.scrapbook
        post.save()
        self.assertEqual(post.title, 'Test Post! @#%^&*()_+{}:"<>?')
        self.assertEqual(post.content, 'Test Post Content! @#%^&*()_+{}:"<>?')
        self.assertEqual(post.status, 1)
        self.assertTrue(post.image is not None)
        self.assertTrue(post.image != '')

    def test_post_form_invalid_image_format(self):
        # Edge Test: Test the PostForm with invalid image format
        image = SimpleUploadedFile(name='test_image.gif', content=b'invalid_image', content_type='image/gif')
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post',
            'content': 'Test Post Content',
            'status': 1,
        }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(form.errors['image'], ['Upload a valid image. The file you uploaded was either not an image or a corrupted image.'])

    def test_post_form_large_image_file(self):
        # Edge Test: Test the PostForm with large image file
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DecompressionBombWarning)
            large_image = Image.new('RGB', (12000, 12000), color='red')  # Create a larger image
            image_io = io.BytesIO()
            large_image.save(image_io, format='JPEG')
            image_content = image_io.getvalue()
            image = SimpleUploadedFile(name='test_image.jpg', content=image_content, content_type='image/jpeg')
            form = PostForm(data={
                'scrapbook': self.scrapbook.id,
                'title': 'Test Post',
                'content': 'Test Post Content',
                'status': 1,
            }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(form.errors['image'], ['Image file too large. Size should not exceed 2.0 MB.'])

class SharedAccessFormTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user1)
        self.post = Post.objects.create(title='Test Post', author=self.user1, scrapbook=self.scrapbook, status=1)

    def test_shared_access_form_valid_data(self):
        # Test the SharedAccessForm with valid data
        form = ShareContentForm(data={
            'user': self.user2.id,
            'scrapbook_id': self.scrapbook.id,
            'post_id': None,
        }, shared_by=self.user1, scrapbook=self.scrapbook)
        self.assertTrue(form.is_valid())
        shared_access = form.save(commit=False)
        shared_access.save()
        self.assertEqual(shared_access.user, self.user2)
        self.assertEqual(shared_access.scrapbook_id, self.scrapbook.id)
        self.assertEqual(shared_access.post_id, None)
        



