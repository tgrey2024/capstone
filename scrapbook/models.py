from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Private"),
    (1, "Public")
)

# Create your models here.
class Scrapbook(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)