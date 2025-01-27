from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import uuid

# Status choices for Scrapbook and Post models
STATUS = (
    (0, "Draft"),
    (1, "Private"),
    (2, "Public")
)


# Validates the status field in Scrapbook and Post models
def validate_status(value):
    if value not in [0, 1, 2]:
        raise ValidationError(f'{value} is not a valid status')


class Scrapbook(models.Model):
    """
    Stores a single scrapbook entry related to :model:`auth.User`.

    Scrapbooks are collections of posts that can be shared with other users.

    Attributes:
        title: A CharField that stores the title of the scrapbook.
        slug: A SlugField that stores the unique slug of the scrapbook.
        image: A CloudinaryField that stores the image of the scrapbook.
        content: A TextField that stores the content of the scrapbook.
        created_on: A DateTimeField that stores the date and time the 
            scrapbook was created.
        updated_on: A DateTimeField that stores the date and time the 
            scrapbook was last updated.
        status: An IntegerField that stores the status of the scrapbook.
        description: A TextField that stores the description of the scrapbook.
    
    Methods:
        __str__: Returns an f-string with the title and author of the
            scrapbook.
        save: Overrides the save method to automatically generate a unique
            slug for the instance if it does not already have one.
        
    Meta:
        ordering: Orders scrapbooks from newest to oldest.

    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = CloudinaryField('scrapbook_image', default='placeholder')
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # orders scrapbooks from newest to oldest
    class Meta:
        ordering = ["-created_on"]

    # returns f-string with title and author from dataset
    def __str__(self):
        return f"{self.title} | by {self.author.username}"

    def save(self, *args, **kwargs):
        self.title = self.title.strip()  # Trim leading and trailing spaces
        # Automatically generate a unique slug if it does not exist
        if not self.slug:
            self.slug = slugify(self.title)
            if Scrapbook.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)


class Post(models.Model):
    """
    Stores a single post entry related to :model:`auth.User`
    and :model:`scrapbook.Scrapbook`.

    Posts are entries that belong to a scrapbook and can be shared with other
    users.

    Attributes:
        scrapbook: A ForeignKey that stores the scrapbook the post belongs to.
        author: A ForeignKey that stores the author of the post.
        title: A CharField that stores the title of the post.
        slug: A SlugField that stores the unique slug of the post.
        image: A CloudinaryField that stores the image of the post.
        created_on: A DateTimeField that stores the date and time the post
            was created.
        updated_on: A DateTimeField that stores the date and time the post
            was last updated.
        status: An IntegerField that stores the status of the post.
        content: A TextField that stores the content of the post.
        approved: A BooleanField that stores whether the post is approved.

    Methods:
        __str__: Returns an f-string with the title, scrapbook title and author
            of the post.
        save: Overrides the save method to automatically generate a unique
            slug for the instance if it does not already have one.
    
    Meta:
        ordering: Orders posts from newest to oldest.

    """
    scrapbook = models.ForeignKey(
        Scrapbook, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = CloudinaryField('post_image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField(max_length=200, blank=True)
    approved = models.BooleanField(default=False)

    # orders posts from newest to oldest
    class Meta:
        ordering = ["-created_on"]

    # returns f-string with title, scrapbook title and author from dataset
    def __str__(self):
        return f"{self.title} | by {self.author.username}"

    
    def save(self, *args, **kwargs):
        self.title = self.title.strip()
        if not self.slug:
            self.slug = slugify(self.title)
            if Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)


class SharedAccess(models.Model):
    """
    Stores a single shared access entry related to :model:`auth.User`,
    :model:`scrapbook.Scrapbook`, :model:`scrapbook.Post` and
    :model:`auth.User`.

    Shared access entries are used to share scrapbooks and posts with other
    users.

    Attributes:
        user: A ForeignKey that stores the user the shared access belongs to.
        scrapbook: A ForeignKey that stores the scrapbook the shared access
            belongs to.
        post: A ForeignKey that stores the post the shared access belongs to.
        shared_by: A ForeignKey that stores the user that shared the access.

    Methods:
        __str__: Returns an f-string with the username, scrapbook title and
            post title of the shared access.
        
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scrapbook = models.ForeignKey(
        Scrapbook, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    shared_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='shared_accesses_shared_by')

    class Meta:
        # Ensures that a user can only have one shared access
        # to a scrapbook
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'scrapbook', 'post'],
                name='unique_shared_access')
        ]

    def __str__(self):
        # returns f-string with username, scrapbook title and post title
        return f"{self.user.username} | {
            self.scrapbook.title if self.scrapbook else 'No Scrapbook'}"
