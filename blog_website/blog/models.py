from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    title_eng = models.CharField(max_length=100, verbose_name='Заголовок на английском')
    text_eng = models.TextField(verbose_name='Текст на английском')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", default="", verbose_name='Автор')
    # photo = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name='Фото')
    # video = models.FileField(upload_to='post_videos/', blank=True, null=True, verbose_name='Видео')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_date = models.DateField(verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/', verbose_name='Изображение')

    def __str__(self):
        return f"Image for post: {self.post}"


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='post_videos/', verbose_name='Видео')

    def __str__(self):
        return f"Video for post: {self.post}"
