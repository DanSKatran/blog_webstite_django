from modeltranslation.translator import TranslationOptions, register

from blog.models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
