from django import forms
from blog.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'email', 'body']
        widgets = {
            'user': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'seo_title', 'seo_description', 'status', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'content': forms.Textarea(attrs={'class': "form-control"}),
            'category': forms.Select(attrs={'class': "form-control"}),
            'status': forms.Select(attrs={'class': "form-control"}),
            'seo_title': forms.TextInput(attrs={'class': "form-control"}),
            'seo_description': forms.Textarea(attrs={'class': "form-control"}),
            'image': forms.FileInput(attrs={'class': "form-control"})
        }