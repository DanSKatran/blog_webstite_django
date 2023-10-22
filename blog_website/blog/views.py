from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


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
        if Post.objects.filter(
            pk=self.kwargs['pk'],
            is_published=True,
            published_date__lte=timezone.now(),
        ).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            return Http404()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.request.resolver_match.view_name
        return context


def page_not_found(request, exception):
    return render(request, 'custom_errors/404.html', status=404)


def server_error(request):
    return render(request, 'custom_errors/500.html', status=500)
