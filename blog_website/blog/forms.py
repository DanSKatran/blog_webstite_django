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
    title_ru = forms.CharField(label='Заголовок', max_length=100)
    text_ru = forms.CharField(label='Текст', widget=forms.Textarea)
    title_en = forms.CharField(label='Заголовок на английском', max_length=100)
    text_en = forms.CharField(label='Текст на английском', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('title_ru', 'text_ru', 'title_en', 'text_en', 'author', 'published_date', 'is_published', 'images', 'videos')
        labels = {
            # "title": "Заголовок",
            # "text": "Текст",
            "author": "Автор",
            "published_date": "Дата публикации",
            "is_published": "Опубликовано",
            "images": "Фото",
            "videos": "Видео"
        }
        widgets = {
            # 'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
            'videos': forms.FileInput(attrs={'class': 'form-control'}),
        }
