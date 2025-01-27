from PIL import Image
from PIL import ImageFile
from PIL.Image import DecompressionBombWarning
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
import io
import warnings
from scrapbook.forms import PostForm, ShareContentForm, ScrapbookForm
from scrapbook.models import Scrapbook, Post, SharedAccess


# Suppress DecompressionBombWarning
warnings.simplefilter('ignore', DecompressionBombWarning)
ImageFile.LOAD_TRUNCATED_IMAGES = True


class ScrapbookFormTest(TestCase):
    """
    Test case for the ScrapbookForm.

    This test case includes tests for validating the ScrapbookForm with
    valid and invalid data, ensuring that the form behaves as expected.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_scrapbook_form_valid_data(self):
        # Test the ScrapbookForm with valid data
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
        form = ScrapbookForm(data={
            'title': 'Test Scrapbook',
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1,
        }, files={'image': image})
        self.assertTrue(form.is_valid())
        scrapbook = form.save(commit=False)
        scrapbook.author = self.user
        scrapbook.save()
        self.assertEqual(scrapbook.title, 'Test Scrapbook')
        self.assertEqual(scrapbook.content, 'Test Scrapbook Content')
        self.assertEqual(scrapbook.description, 'Test Scrapbook Description')
        self.assertEqual(scrapbook.status, 1)
        self.assertTrue(scrapbook.image is not None)
        self.assertTrue(scrapbook.image != '')

    def test_scrapbook_form_invalid_data(self):
        # Test the ScrapbookForm with invalid data
        form = ScrapbookForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_scrapbook_form_missing_title(self):
        # Test the ScrapbookForm with missing title
        form = ScrapbookForm(data={
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_scrapbook_form_missing_image(self):
        # Test the ScrapbookForm with missing image
        form = ScrapbookForm(data={
            'title': 'Test Scrapbook',
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(form.errors['image'], ['This field is required.'])

    # Edge Tests
    def test_scrapbook_form_max_length_title(self):
        # Edge Test: Test the ScrapbookForm with maximum length title
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
        form = ScrapbookForm(data={
            'title': 'a' * 100,
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1,
        }, files={'image': image})
        self.assertTrue(form.is_valid())

    def test_scrapbook_form_exceed_length_title(self):
        # Edge Test: Test the ScrapbookForm with exceeding length title
        form = ScrapbookForm(data={
            'title': 'a' * 101,
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], [
            "The title cannot be more than 100 characters."])

    def test_scrapbook_form_special_characters(self):
        # Edge Test: Test the ScrapbookForm with
        # special characters in title and content
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
        form = ScrapbookForm(data={
            'title': 'Test Scrapbook! @#%^&*()_+{}:"<>?',
            'content': 'Test Scrapbook Content! @#%^&*()_+{}:"<>?',
            'description': 'Test Scrapbook Description! @#%^&*()_+{}:"<>?',
            'status': 1,
        }, files={'image': image})
        self.assertTrue(form.is_valid())
        scrapbook = form.save(commit=False)
        scrapbook.author = self.user
        scrapbook.save()
        self.assertEqual(
            scrapbook.title, 'Test Scrapbook! @#%^&*()_+{}:"<>?')
        self.assertEqual(
            scrapbook.content, 'Test Scrapbook Content! @#%^&*()_+{}:"<>?')
        self.assertEqual(
            scrapbook.description,
            'Test Scrapbook Description! @#%^&*()_+{}:"<>?')
        self.assertEqual(scrapbook.status, 1)
        self.assertTrue(scrapbook.image is not None)
        self.assertTrue(scrapbook.image != '')

    def test_scrapbook_form_invalid_image_format(self):
        # Edge Test: Test the ScrapbookForm with invalid image format
        image = SimpleUploadedFile(
            name='test_image.gif',
            content=b'invalid_image',
            content_type='image/gif')
        form = ScrapbookForm(data={
            'title': 'Test Scrapbook',
            'content': 'Test Scrapbook Content',
            'description': 'Test Scrapbook Description',
            'status': 1,
        }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(
            form.errors['image'], [
                'Upload a valid image or an uncorrupted image.'])

    def test_scrapbook_form_large_image_file(self):
        # Edge Test: Test the ScrapbookForm with large image file
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DecompressionBombWarning)
            large_image = Image.new('RGB', (12000, 12000), color='red')
            image_io = io.BytesIO()
            large_image.save(image_io, format='JPEG')
            image_content = image_io.getvalue()
            image = SimpleUploadedFile(
                name='test_image.jpg',
                content=image_content,
                content_type='image/jpeg')
            form = ScrapbookForm(data={
                'title': 'Test Scrapbook',
                'content': 'Test Scrapbook Content',
                'description': 'Test Scrapbook Description',
                'status': 1,
            }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(
            form.errors['image'], [
                'Image file too large. Size should not exceed 2.0 MB.'])


class PostFormTest(TestCase):
    """
    Test case for the PostForm.

    This test case includes tests for validating the PostForm with
    valid and invalid data, ensuring that the form behaves as expected.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass')
        self.scrapbook = Scrapbook.objects.create(
            title='Test Scrapbook',
            author=self.user)

    def test_post_form_valid_data(self):
        # Test the PostForm with valid data
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
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
        self.assertEqual(len(form.errors), 4)

    def test_post_form_missing_title(self):
        # Test the PostForm with missing title
        form = PostForm(
            data={'content': 'Test Post Content', 'status': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertEqual(
            form.errors['title'], ['This field is required.'])

    def test_post_form_missing_image(self):
        # Test the PostForm with missing image
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post',
            'content': 'Test Post Content',
            'status': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(
            form.errors['image'], ['This field is required.'])

    # Edge Tests
    def test_post_form_max_length_title(self):
        # Edge Test: Test the PostForm with maximum length title
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'a' * 100,
            'content': 'Test Post Content',
            'status': 1,
        }, files={'image': image})
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
        # Edge Test: Test the PostForm with
        # special characters in title and content
        image_content = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
            b'\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_content,
            content_type='image/jpeg'
        )
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post! @#%^&*()_+{}:"<>?',
            'content': 'Test Post Content! @#%^&*()_+{}:"<>?',
            'status': 1,
        }, files={'image': image})
        self.assertTrue(form.is_valid())
        post = form.save(commit=False)
        post.author = self.user
        post.scrapbook = self.scrapbook
        post.save()
        self.assertEqual(post.title, 'Test Post! @#%^&*()_+{}:"<>?')
        self.assertEqual(
            post.content, 'Test Post Content! @#%^&*()_+{}:"<>?')
        self.assertEqual(post.status, 1)
        self.assertTrue(post.image is not None)
        self.assertTrue(post.image != '')

    def test_post_form_invalid_image_format(self):
        # Edge Test: Test the PostForm with invalid image format
        image = SimpleUploadedFile(
            name='test_image.gif',
            content=b'invalid_image',
            content_type='image/gif')
        form = PostForm(data={
            'scrapbook': self.scrapbook.id,
            'title': 'Test Post',
            'content': 'Test Post Content',
            'status': 1,
        }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(
            form.errors['image'],
            ['Upload a valid image or an uncorrupted image.'])

    def test_post_form_large_image_file(self):
        # Edge Test: Test the PostForm with large image file
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DecompressionBombWarning)
            large_image = Image.new('RGB', (12000, 12000), color='red')
            image_io = io.BytesIO()
            large_image.save(image_io, format='JPEG')
            image_content = image_io.getvalue()
            image = SimpleUploadedFile(
                name='test_image.jpg',
                content=image_content,
                content_type='image/jpeg')
            form = PostForm(data={
                'scrapbook': self.scrapbook.id,
                'title': 'Test Post',
                'content': 'Test Post Content',
                'status': 1,
            }, files={'image': image})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
        self.assertEqual(
            form.errors['image'],
            ['Image file too large. Size should not exceed 2.0 MB.'])


class SharedAccessFormTest(TestCase):
    """
    Test case for the SharedAccessForm.

    This test case includes tests for validating the SharedAccessForm with
    valid and invalid data, ensuring that the form behaves as expected.
    """

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass')
        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass')
        self.scrapbook = Scrapbook.objects.create(
            title='Test Scrapbook',
            author=self.user1)
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user1,
            scrapbook=self.scrapbook,
            status=1)

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
        self.assertEqual(shared_access.shared_by, self.user1)

    def test_shared_access_form_invalid_data(self):
        # Test the SharedAccessForm with invalid data
        form = ShareContentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_shared_access_form_missing_user(self):
        # Test the SharedAccessForm with missing user
        form = ShareContentForm(
            data={'scrapbook_id': self.scrapbook.id, 'post_id': None},
            shared_by=self.user1,
            scrapbook=self.scrapbook)
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors)
        self.assertEqual(
            form.errors['user'], ['This field is required.'])

    def test_shared_access_form_existing_shared_access(self):
        # Test the SharedAccessForm with existing shared access
        SharedAccess.objects.create(
            user=self.user2,
            scrapbook=self.scrapbook,
            shared_by=self.user1)
        form = ShareContentForm(data={
            'user': self.user2.id,
            'scrapbook_id': self.scrapbook.id,
            'post_id': None,
        }, shared_by=self.user1, scrapbook=self.scrapbook)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(
            form.errors['__all__'],
            ['This scrapbook has already been shared with this user.'])
