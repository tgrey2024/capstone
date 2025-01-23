from django import forms
from .models import Post, Scrapbook, SharedAccess
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from cloudinary import CloudinaryResource
from PIL import Image

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
        error_messages={'max_length': "The title cannot be more than 100 characters."}
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Post
        fields = ('scrapbook', 'title', 'content', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        scrapbook = kwargs.pop('scrapbook', None)
        super().__init__(*args, **kwargs)
        if scrapbook:
            self.fields['scrapbook'].initial = scrapbook
        if self.instance and self.instance.pk:
            self.fields['image'].required = False

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise forms.ValidationError("The title cannot be more than 100 characters.")
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image and self.instance.pk:
            return self.instance.image
        if image:
            if isinstance(image, CloudinaryResource):
                return image
            if hasattr(image, 'size'):
                if image.size > 2 * 1024 * 1024:  # 2MB
                    raise forms.ValidationError("Image file too large. Size should not exceed 2.0 MB.")
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                raise forms.ValidationError("Upload a valid image. The file you uploaded was either not an image or a corrupted image.")
        return image

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            content = ''
        return content

class ScrapbookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'max_length': "The title cannot be more than 100 characters."}
    )

    class Meta:
        model = Scrapbook
        fields = ('title', 'content', 'description', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),            
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image and self.instance.pk:
            return self.instance.image
        if image:
            if isinstance(image, CloudinaryResource):
                return image
            if hasattr(image, 'size'):
                if image.size > 2 * 1024 * 1024:  # 2MB
                    raise forms.ValidationError("Image file too large. Size should not exceed 2.0 MB.")
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                raise forms.ValidationError("Upload a valid image. The file you uploaded was either not an image or a corrupted image.")
        return image

from django import forms
from .models import SharedAccess, Scrapbook, Post
from django.contrib.auth.models import User

class ShareContentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    scrapbook_id = forms.IntegerField(widget=forms.HiddenInput())
    post_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = SharedAccess
        fields = ['user', 'scrapbook_id', 'post_id']

    def __init__(self, *args, **kwargs):
        shared_by = kwargs.pop('shared_by', None)
        scrapbook = kwargs.pop('scrapbook', None)
        super().__init__(*args, **kwargs)
        if shared_by:
            self.fields['user'].queryset = User.objects.exclude(id=shared_by.id)
        if scrapbook:
            self.fields['scrapbook_id'].initial = scrapbook.id
        self.fields['post_id'].initial = None  # Hide post_id as all posts in the scrapbook are automatically shared

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.scrapbook = Scrapbook.objects.get(id=self.cleaned_data['scrapbook_id'])
        instance.post = None  # Set post to None as all posts in the scrapbook are automatically shared
        if commit:
            instance.save()
            # Create SharedAccess instances for each post in the scrapbook
            posts = Post.objects.filter(scrapbook=instance.scrapbook)
            for post in posts:
                SharedAccess.objects.create(
                    user=instance.user,
                    scrapbook=instance.scrapbook,
                    post=post,
                    shared_by=instance.shared_by
                )
        return instance