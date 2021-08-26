from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import (
    PostListView,
    PostDetailListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, AddCommentLike, AddCommentDislike, CommentReplyView
)
from . import views
from .views import AddLike, AddDislike

urlpatterns = [
    path('home/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailListView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
]
