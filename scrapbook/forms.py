from .models import Post
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
        fields = ('title', 'content', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise forms.ValidationError("The title cannot be more than 100 characters.")
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            print(f"Image size: {image.size}")
            if image.size > 2 * 1024 * 1024:  # 2MB
                print("Image file too large.")
                raise forms.ValidationError("Image file too large. Size should not exceed 2.0 MB.")
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                print(f"Image validation error: {e}")
                raise forms.ValidationError("Upload a valid image. The file you uploaded was either not an image or a corrupted image.")
        return image