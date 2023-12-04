import os
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", default="", verbose_name='Автор')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_date = models.DateField(verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    video_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class CustomFileSystemStorage(models.FileField):
    def delete(self, name):
        try:
            super().delete(name)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = CustomFileSystemStorage(_("Image"), upload_to='post_images/')

    def __str__(self):
        return f"Image for post: {self.post}"


@receiver(models.signals.post_delete, sender=PostImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `PostImage` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=PostImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `PostImage` object is updated
    with a new file.
    """
    if not instance.pk:
        return False

    try:
        old_image = PostImage.objects.get(pk=instance.pk).image
    except PostImage.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    video = CustomFileSystemStorage(_("Video"), upload_to='post_videos/')

    def __str__(self):
        return f"Video for post: {self.post}"


@receiver(models.signals.post_delete, sender=PostVideo)
def auto_delete_file_on_delete_video(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `PostVideo` object is deleted.
    """
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)


@receiver(models.signals.pre_save, sender=PostVideo)
def auto_delete_file_on_change_video(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `PostVideo` object is updated
    with a new file.
    """
    if not instance.pk:
        return False

    try:
        old_video = PostVideo.objects.get(pk=instance.pk).video
    except PostVideo.DoesNotExist:
        return False

    new_video = instance.video
    if not old_video == new_video:
        if os.path.isfile(old_video.path):
            os.remove(old_video.path)
