from django.http import Http404, FileResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone

from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post

from django.http import HttpResponse, HttpResponseNotFound
from django.utils.http import http_date
from django.views import View
from django.conf import settings
import os


class MainPageView(TemplateView):
    template_name = 'blog/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        return context


class AboutPageView(TemplateView):
    template_name = 'blog/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        return context


class ContactPageView(TemplateView):
    template_name = 'blog/contacts_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        return context


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True,
            published_date__lte=timezone.now(),
        ).order_by('-published_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        return context


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post.objects.select_related('author'),
            pk=self.kwargs['pk'],
            is_published=True,
            published_date__lte=timezone.now(),
        )
        self.object = post
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        context['images'] = self.object.images.all().prefetch_related('image')
        context['videos'] = self.object.videos.all().prefetch_related('video')
        return context


def page_not_found(request, exception):
    return render(request, 'custom_errors/404.html', status=404)


def server_error(request):
    return render(request, 'custom_errors/500.html', status=500)


class RangeFileView(View):
    def get(self, request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)

        if not os.path.exists(file_path):
            return HttpResponseNotFound("File not found")

        response = HttpResponse()
        response['Accept-Ranges'] = 'bytes'

        try:
            with open(file_path, 'rb') as file:
                response.write(file.read())
        except FileNotFoundError:
            return HttpResponseNotFound("File not found")

        return response


# def view_image(request, url):
#     # url = request.GET.get('url', '')
#     print(url)
#     image_path = url
#     with open(image_path, 'rb') as image_file:
#         return FileResponse(image_file, content_type='image/png')
