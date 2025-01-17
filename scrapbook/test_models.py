import re
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Scrapbook, Post

class ScrapbookModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_scrapbook_creation(self):
        # Test the creation of a Scrapbook instance
        self.assertEqual(Scrapbook.objects.count(), 0)
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertEqual(Scrapbook.objects.count(), 1)
        self.assertEqual(scrapbook.title, 'Test Scrapbook')
        self.assertEqual(scrapbook.author, self.user)
        self.assertEqual(scrapbook.slug, 'test-scrapbook')
        self.assertEqual(scrapbook.status, 1)
        self.assertEqual(scrapbook.content, '')
        self.assertEqual(scrapbook.description, '')
        self.assertIsNotNone(scrapbook.created_on)
        self.assertIsNotNone(scrapbook.updated_on)
        self.assertEqual(str(scrapbook), 'Test Scrapbook | by testuser')
        self.assertEqual(scrapbook.image, 'placeholder')

    def test_scrapbook_str(self):
        # Test the __str__ method of the Scrapbook model
        self.assertEqual(str(Scrapbook(title='Test Scrapbook', author=self.user)), 'Test Scrapbook | by testuser')

    def test_scrapbook_slug_generation(self):
        # Test the slug generation for a Scrapbook instance
        self.assertEqual(Scrapbook.objects.count(), 0)
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertEqual(scrapbook.slug, 'test-scrapbook')
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertTrue(re.match(r'^test-scrapbook-[a-f0-9]{8}$', scrapbook.slug))
        self.assertEqual(len(scrapbook.slug), 23)

    def test_scrapbook_unique_slug(self):
        # Test the uniqueness of the slug for a Scrapbook instance
        self.assertEqual(Scrapbook.objects.count(), 0)
        scrapbook1 = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        scrapbook2 = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertNotEqual(scrapbook1.slug, scrapbook2.slug)

    def test_scrapbook_ordering(self):
        # Test the ordering of Scrapbook instances
        scrapbook1 = Scrapbook.objects.create(title='Test Scrapbook 1', author=self.user)
        scrapbook2 = Scrapbook.objects.create(title='Test Scrapbook 2', author=self.user)
        scrapbook3 = Scrapbook.objects.create(title='Test Scrapbook 3', author=self.user)
        self.assertEqual(list(Scrapbook.objects.all()), [scrapbook3, scrapbook2, scrapbook1])

    def test_scrapbook_author_relationship(self):
        # Test the relationship between Scrapbook and User (author)
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertEqual(scrapbook.author, self.user)
        self.assertEqual(list(self.user.scrapbook_set.all()), [scrapbook])

    def test_scrapbook_default_values(self):
        # Test the default values of Scrapbook fields
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertEqual(scrapbook.status, 1)
        self.assertEqual(scrapbook.content, '')
        self.assertEqual(scrapbook.description, '')
        self.assertEqual(scrapbook.image, 'placeholder')

    def test_scrapbook_blank_fields(self):
        # Test the blank fields of Scrapbook
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertEqual(scrapbook.content, '')
        self.assertEqual(scrapbook.description, '')

    def test_scrapbook_title_length(self):
        # Edge test for the maximum length of the title field
        title = 'a' * 101
        scrapbook = Scrapbook(title=title, author=self.user)
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()  # This will run the model's validation

    def test_post_slug_length(self):
        # Edge test for the maximum length of the slug field
        slug = 'a' * 101
        scrapbook = Scrapbook(slug=slug, author=self.user)
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()  # This will run the model's validation

class PostModelTest(TestCase):

    def setUp(self):
        # Create a user and a scrapbook for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)

    def test_post_creation(self):
        # Test the creation of a Post instance
        self.assertEqual(self.scrapbook.posts.count(), 0)
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(self.scrapbook.posts.count(), 1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.status, 1)
        self.assertIsNotNone(post.created_on)
        self.assertIsNotNone(post.updated_on)
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(post.image, 'placeholder')

    def test_post_str(self):
        # Test the __str__ method of the Post model
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(str(post), 'Test Post')

    def test_post_slug_generation(self):
        # Test the slug generation for a Post instance
        self.assertEqual(self.scrapbook.posts.count(), 0)
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(post.slug, 'test-post')
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertTrue(re.match(r'^test-post-[a-f0-9]{8}$', post.slug))
        self.assertEqual(len(post.slug), 18)

    def test_post_unique_slug(self):
        # Test the uniqueness of the slug for a Post instance
        self.assertEqual(self.scrapbook.posts.count(), 0)
        post1 = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        post2 = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertNotEqual(post1.slug, post2.slug)

    def test_post_ordering(self):
        # Test the ordering of Post instances
        post1 = self.scrapbook.posts.create(title='Test Post 1', author=self.user, status=1)
        post2 = self.scrapbook.posts.create(title='Test Post 2', author=self.user, status=1)
        post3 = self.scrapbook.posts.create(title='Test Post 3', author=self.user, status=1)
        self.assertEqual(list(self.scrapbook.posts.all()), [post3, post2, post1])

    def test_post_author_relationship(self):
        # Test the relationship between Post and User (author)
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(post.author, self.user)
        self.assertEqual(list(self.user.post_author.all()), [post])

    def test_post_scrapbook_relationship(self):
        # Test the relationship between Post and Scrapbook
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(post.scrapbook, self.scrapbook)
        self.assertEqual(list(self.scrapbook.posts.all()), [post])

    def test_post_default_values(self):
        # Test the default values of Post fields
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(post.status, 1)
        self.assertEqual(post.image, 'placeholder')

    def test_post_blank_fields(self):
        # Test the blank fields of Post
        post = self.scrapbook.posts.create(title='Test Post', author=self.user, status=1)
        self.assertEqual(post.content, '')

    def test_post_title_length(self):
        # Edge test for the maximum length of the title field
        title = 'a' * 101
        post = Post(title=title, author=self.user)
        with self.assertRaises(ValidationError):
            post.full_clean()  # This will run the model's validation
    
    def test_post_slug_length(self):
        # Edge test for the maximum length of the slug field
        slug = 'a' * 101
        post = Post(slug=slug, author=self.user)
        with self.assertRaises(ValidationError):
            post.full_clean()  # This will run the model's validation