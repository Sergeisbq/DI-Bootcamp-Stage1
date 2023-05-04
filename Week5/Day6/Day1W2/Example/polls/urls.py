from django.urls import path
from polls.views import PostCreateView, PostListView, PostView, PostUpdateView, add_comment

urlpatterns = [
    path("add-post/", PostCreateView.as_view()),
    path("", PostListView.as_view(), name="posts-all"),
    path("post/<slug:slug>", PostView.as_view(), name="post"), 
    path("post-update/<slug:slug>", PostUpdateView.as_view()),
    path("add_comment/", add_comment, name="add_comment")

]