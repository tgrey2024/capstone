from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Private"),
    (2, "Public")
)

# Create your models here.
class Scrapbook(models.Model):
    """
    Stores a single scrapbook entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    """
    Stores a single post entry related to :model:`auth.User` and :model:`blog.Post`.
    """
    scrapbook = models.ForeignKey(Scrapbook, on_delete=models.CASCADE, related_name="post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=-1)
    content = models.TextField(max_length=200, blank=True)
    approved = models.BooleanField(default=False)
    

class Image(models.Model):
    """
    Stores a single image entry related to :model:`scrapbook.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_image")
    featured_image = CloudinaryField('image', default='placeholder')
    caption = models.TextField(max_length=200, blank=True)
    is_puzzle = models.BooleanField(default=False)

