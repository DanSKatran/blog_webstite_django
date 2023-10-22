from django import forms

from blog_website.blog.models import Post, PostImage, PostVideo


class PostForm(forms.ModelForm):
    """post creating form"""
    images = forms.ModelMultipleChoiceField(
        queryset=PostImage.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    videos = forms.ModelMultipleChoiceField(
        queryset=PostVideo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    model = Post
    fields = ('title', 'text', 'title_eng', 'text_eng', 'author', 'published_date', 'is_published', 'images', 'videos')
    labels = {
        "title": "Заголовок",
        "text": "Текст",
        "title_eng": "Заголовок на английском",
        "text_eng": "Текст на английском",
        "author": "Автор",
        "published_date": "Дата публикации",
        "is_published": "Опубликовано",
        "images": "Фото",
        "videos": "Видео"
    }
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'text': forms.Textarea(attrs={'class': 'form-control'}),
        'title_eng': forms.TextInput(attrs={'class': 'form-control'}),
        'text_eng': forms.Textarea(attrs={'class': 'form-control'}),
        'author': forms.Select(attrs={'class': 'form-control'}),
        'published_date': forms.DateInput(attrs={'class': 'form-control'}),
        'is_published': forms.CheckboxInput(attrs={'class': 'form-control'}),
        'images': forms.FileInput(attrs={'class': 'form-control'}),
        'videos': forms.FileInput(attrs={'class': 'form-control'}),
    }

