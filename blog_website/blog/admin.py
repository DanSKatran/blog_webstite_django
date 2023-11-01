from django.contrib import admin
from .models import Post, PostImage, PostVideo
from modeltranslation.admin import TranslationAdmin


class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 1


class PostVideoInline(admin.StackedInline):
    model = PostVideo
    extra = 1


class PostAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published', 'created_date')
    list_filter = ('published_date', 'is_published', 'created_date')
    search_fields = ('title', 'created_date')
    date_hierarchy = 'created_date'

    inlines = [PostImageInline, PostVideoInline]

    fieldsets = [
        ('Основная информация', {
            'fields': ('title', 'text', 'author', 'published_date', 'is_published')
        }),
    ]


admin.site.register(Post, PostAdmin)
