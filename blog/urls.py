from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogCreateView, CreateBlogList, \
    toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list',BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>',BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('createblogs/', CreateBlogList, name='createblogs'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity')
]