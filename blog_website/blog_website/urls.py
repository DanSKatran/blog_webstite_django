from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve
from django.contrib.staticfiles.views import serve

from blog.views import RangeFileView

handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('blog.urls', namespace='blog')),
    re_path(r'^media/(?P<path>.*)$', RangeFileView.as_view(), name='media'),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += i18n_patterns(
    path('', include('blog.urls')),
)


# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$',
#             serve, {'document_root': settings.MEDIA_ROOT, }),
# ]
# urlpatterns += [
#     re_path(r'^static/(?P<path>.*)$',
#             serve, {'document_root': settings.STATIC_ROOT, }),
# ]
