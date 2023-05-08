from django.contrib import admin
from django.urls import path, include
from posts.views import PostListView, PostDetailView, AuthorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('api/author/<int:pk>/', AuthorView.as_view(), name='author')
]
