from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('gallery/', views.PostListView.as_view(), name='post_list'),
    path('gallery/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    ]
