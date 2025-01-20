from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

STATUS = (
    (0, "Draft"),
    (1, "Private"),
    (2, "Public")
)

def validate_status(value):
    if value not in [0, 1, 2]:
        raise ValidationError(f'{value} is not a valid status')

class Scrapbook(models.Model):
    """
    Stores a single scrapbook entry related to :model:`auth.User`.
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
    Stores a single post entry related to :model:`auth.User` and :model:`blog.Post`.
    """
    scrapbook = models.ForeignKey(Scrapbook, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = CloudinaryField('post_image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS)
    content = models.TextField(max_length=200, blank=True)
    approved = models.BooleanField(default=False)
    
    # orders posts from newest to oldest
    class Meta:
        ordering = ["-created_on"]

    # returns f-string with title, scrapbook title and author from dataset
    def __str__(self):
        return self.title   

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically generate a unique slug for the instance if it does not already have one.
        
        If the slug is not set, it generates a slug from the title. If a post with the same slug already exists, 
        it appends a unique identifier to the slug to ensure uniqueness.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
        Returns:
            None
        """
        # Automatically generate a unique slug if it does not exist
        if not self.slug:
            self.slug = slugify(self.title)
            if Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
