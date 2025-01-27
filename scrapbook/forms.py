from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from cloudinary import CloudinaryResource
from PIL import Image
from .models import Post, Scrapbook, SharedAccess


class ScrapbookForm(forms.ModelForm):
    """
    Form for creating and updating a scrapbook.

    Fields:
    title -- The title of the scrapbook.
    image -- The cover image of the scrapbook.
    content -- The content of the scrapbook.
    description -- A note to self about the scrapbook.
    status -- The status of the scrapbook (public or private).

    Methods:
    clean_image -- Validate the cover image.

    """
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={
            'max_length':
            "The title cannot be more than 100 characters."}
    )
    image = forms.FileField(
        label="Scrapbook Cover Image",
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=True,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}), required=False)

    description = forms.CharField(
        label="Note to Self (Only you can see this)",
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Scrapbook
        fields = ('title', 'content', 'description', 'status', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'id_image'}),
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
                    raise forms.ValidationError(
                        "Image file too large. Size should not exceed 2.0 MB.")
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                raise forms.ValidationError(
                    "Upload a valid image or an uncorrupted image.")
        return image


class PostForm(forms.ModelForm):
    """
    Form for creating and updating a post.

    Fields:
    title -- The title of the post.
    image -- The image of the post.
    content -- The content of the post.
    status -- The status of the post (public or private).

    Methods:
    clean_image -- Validate the post image.
    clean_title -- Validate the post title.
    clean_content -- Validate the post content.
    """
    title = forms.CharField(
        label="Post Title",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}), required=True,
        error_messages={
            'max_length': "The title cannot be more than 100 characters."}
    )
    image = forms.FileField(
        label="Post Image",
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=True,
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label="Post Content",
        required=False,
    )

    class Meta:
        model = Post
        fields = ('scrapbook', 'title', 'content', 'status', 'image')
        widgets = {
            'scrapbook': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control', 'id': 'id_image'}),
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
            raise forms.ValidationError(
                "The title cannot be more than 100 characters.")
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
                    raise forms.ValidationError(
                        "Image file too large. Size should not exceed 2.0 MB.")
            try:
                img = Image.open(image)
                img.verify()
            except Exception as e:
                raise forms.ValidationError(
                    "Upload a valid image or an uncorrupted image.")
        return image

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            content = ''
        return content


class ShareContentForm(forms.ModelForm):
    """
    Form for sharing a scrapbook or post with another user.

    Fields:
    user -- The user to share the scrapbook or post with.
    scrapbook_id -- The ID of the scrapbook to share.
    post_id -- The ID of the post to share.

    Methods:
    clean -- Validate the user and scrapbook/post combination.
    save -- Save the shared access instance and create shared access instances
    for each post in the scrapbook.
    """
    user = forms.ModelChoiceField(
        queryset=User.objects.none(), widget=forms.Select(attrs={
            'class': 'form-control'}))
    scrapbook_id = forms.IntegerField(widget=forms.HiddenInput())
    post_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = SharedAccess
        fields = ['user', 'scrapbook_id', 'post_id']

    def __init__(self, *args, **kwargs):
        self.shared_by = kwargs.pop('shared_by', None)
        scrapbook = kwargs.pop('scrapbook', None)
        super().__init__(*args, **kwargs)
        # Exclude the user sharing the scrapbook from the user queryset
        if self.shared_by:
            self.fields['user'].queryset = User.objects.exclude(
                id=self.shared_by.id)
        # Set the initial values for the form fields
        if scrapbook:
            self.fields['scrapbook_id'].initial = scrapbook.id
        self.fields['post_id'].initial = None
        # Hide post_id as all posts in the scrapbook are automatically shared

    def clean(self):
        # Validate the user and scrapbook combination
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        scrapbook_id = cleaned_data.get('scrapbook_id')
        if user and scrapbook_id:
            if SharedAccess.objects.filter(
                user=user, scrapbook_id=scrapbook_id
            ).exists():
                raise forms.ValidationError(
                    "This scrapbook has already been shared with this user.")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.scrapbook = Scrapbook.objects.get(
            id=self.cleaned_data['scrapbook_id'])
        instance.post = None
        # Set post to None as all posts in the scrapbook are
        # automatically shared
        instance.shared_by = self.shared_by  # Set the shared_by field
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
                instance.save()
        return instance


class CustomSignupForm(SignupForm):
    """
    Custom signup form for the user registration page.

    Fields:
    username -- The username of the user.
    email -- The email address of the user.

    Methods:
    save -- Save the user instance and perform any additional custom
    processing.

    """

    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Add any additional custom processing here
        return user