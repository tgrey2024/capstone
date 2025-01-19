from .models import Post, Scrapbook
from django import forms
from PIL import Image

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'max_length': "The title cannot be more than 100 characters."}
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Post
        fields = ('scrapbook', 'title', 'image', 'content', 'status')
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
            if hasattr(image, 'file') and hasattr(image.file, 'size'):
                if image.file.size > 2 * 1024 * 1024:  # 2MB
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
            raise forms.ValidationError("This field is required.")
        return content

class ScrapbookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'max_length': "The title cannot be more than 100 characters."}
    )

    class Meta:
        model = Scrapbook
        fields = ('title', 'image', 'status', 'content', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                raise forms.ValidationError("Upload a valid image. The file you uploaded was either not an image or a corrupted image.")
        return image