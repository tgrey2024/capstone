import re
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import Scrapbook, Post, SharedAccess

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

    # Edge tests
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

    def test_scrapbook_special_characters(self):
        # Edge test for the title field with special characters
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook! @#%^&*()_+{}:"<>?', author=self.user)
        self.assertEqual(scrapbook.title, 'Test Scrapbook! @#%^&*()_+{}:"<>?')

    def test_scrapbook_title_spaces(self):
        # Edge test for the title field with leading and trailing spaces
        scrapbook = Scrapbook.objects.create(title='  Test Scrapbook  ', author=self.user)
        self.assertEqual(scrapbook.title, 'Test Scrapbook')

    def test_scrapbook_title_max_length(self):
        # Edge test for the maximum length of the title field
        title = 'a' * 100
        scrapbook = Scrapbook(title=title, author=self.user)
        self.assertTrue(scrapbook.title, title)

    def test_scrapbook_title_exceed_length(self):
        # Edge test for the maximum length of the title field
        title = 'a' * 101
        scrapbook = Scrapbook(title=title, author=self.user)
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()

    def test_scrapbook_description_special_characters(self):
        # Edge test to ensure that the description field can handle special characters and does not raise validation errors.
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user, description='Test Scrapbook! @#%^&*()_+{}:"<>?')
        self.assertEqual(scrapbook.description, 'Test Scrapbook! @#%^&*()_+{}:"<>?')

    def test_scrapbook_description_max_length(self):
        # Edge test to ensure that the description field accepts a description that is exactly at the maximum length limit.
        description = 'a' * 500
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user, description=description)
        self.assertEqual(scrapbook.description, description)

    # Test Scrapbook Description Exceeding Maximum Length:
    def test_scrapbook_description_exceed_length(self):
        # Ensure that the description field raises a validation error when the description exceeds the maximum length limit.
        description = 'a' * 501
        scrapbook = Scrapbook(title='Test Scrapbook', author=self.user, description=description)
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()

    def test_scrapbook_invalid_image_format(self):
        # Edge test to ensure that the image field raises a validation error when an invalid image format is uploaded.
        scrapbook = Scrapbook(title='Test Scrapbook', author=self.user, image='test.pdf')
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()

    def test_scrapbook_large_image_file(self):
        # Edge test to ensure that the image field raises a validation error when an image file exceeds the maximum allowed size.
        scrapbook = Scrapbook(title='Test Scrapbook', author=self.user, image='test.jpg')
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()

    def test_scrapbook_missing_author(self):
        # Edge test to ensure that the scrapbook cannot be created without an author and raises a validation error.
        with self.assertRaises(IntegrityError):
            Scrapbook.objects.create(title='Test Scrapbook')

    def test_scrapbook_invalid_status(self):
        # Edge test to ensure that the status field raises a validation error when an invalid status value is provided.
        scrapbook = Scrapbook(title='Test Scrapbook', author=self.user, status=3)
        with self.assertRaises(ValidationError):
            scrapbook.full_clean()

    # Test Scrapbook Slug Uniqueness:
    def test_scrapbook_unique_slug(self):
        # Edge test to ensure that the slug field generates unique slugs for scrapbooks with the same title.
        scrapbook1 = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        scrapbook2 = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertNotEqual(scrapbook1.slug, scrapbook2.slug)

    def test_scrapbook_created_on(self):
        # Edge test to ensure that the created_on field is automatically set to the current date and time when a scrapbook is created.
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        self.assertIsNotNone(scrapbook.created_on)

    def test_scrapbook_updated_on(self):
        # Edge test to ensure that the updated_on field is automatically updated to the current date and time when a scrapbook is modified.
        scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user)
        scrapbook.title = 'Updated Scrapbook'
        scrapbook.save()
        self.assertIsNotNone(scrapbook.updated_on)

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

class SharedAccessModelTest(TestCase):

    def setUp(self):
        # Create users for testing
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
        
        # Create a scrapbook for testing
        self.scrapbook = Scrapbook.objects.create(title='Test Scrapbook', author=self.user1)
        
        # Create a post for testing
        self.post = Post.objects.create(title='Test Post', author=self.user1, scrapbook=self.scrapbook, status=1)

    def test_shared_access_creation(self):
        # Test the creation of a SharedAccess instance
        self.assertEqual(SharedAccess.objects.count(), 0)
        shared_access = SharedAccess.objects.create(user=self.user2, scrapbook=self.scrapbook, shared_by=self.user1)
        self.assertEqual(SharedAccess.objects.count(), 1)
        self.assertEqual(shared_access.user, self.user2)
        self.assertEqual(shared_access.scrapbook, self.scrapbook)

    def test_shared_access_user_relationship(self):
        # Test the relationship between SharedAccess and User
        shared_access = SharedAccess.objects.create(user=self.user2, scrapbook=self.scrapbook, shared_by=self.user1)
        self.assertEqual(shared_access.user, self.user2)
        self.assertEqual(list(self.user1.shared_accesses_shared_by.all()), [shared_access])
        

    def test_shared_access_scrapbook_relationship(self):
        # Test the relationship between SharedAccess and Scrapbook
        shared_access = SharedAccess.objects.create(user=self.user2, scrapbook=self.scrapbook, shared_by=self.user1)
        self.assertEqual(shared_access.scrapbook, self.scrapbook)
        self.assertEqual(list(self.scrapbook.sharedaccess_set.all()), [shared_access])


    def test_shared_access_post_relationship(self):
        # Test the relationship between SharedAccess and Post
        shared_access = SharedAccess.objects.create(user=self.user2, post=self.post, shared_by=self.user1)
        self.assertEqual(shared_access.post, self.post)


    def test_shared_access_shared_by_relationship(self):
        # Test the relationship between SharedAccess and the user who shared the content
        shared_access = SharedAccess.objects.create(user=self.user2, scrapbook=self.scrapbook, shared_by=self.user1)
        self.assertEqual(shared_access.shared_by, self.user1)
        self.assertEqual(list(self.user1.shared_accesses_shared_by.all()), [shared_access])

    def test_shared_access_str_method(self):
        # Test the __str__ method of the SharedAccess model
        shared_access = SharedAccess.objects.create(user=self.user2, scrapbook=self.scrapbook, shared_by=self.user1)
        self.assertEqual(str(shared_access), 'user2 | Test Scrapbook')
