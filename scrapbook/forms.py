from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Post
        fields = ('title', 'content', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }