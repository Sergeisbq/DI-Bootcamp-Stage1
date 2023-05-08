from django.shortcuts import render, redirect
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)

from .permissions import IsYossi, IsBen

from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED,
                                   HTTP_400_BAD_REQUEST)

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import mixins

# CRUD - CREATE - RETRIEVE - UPDATE - DELETE/DESTROY

class PostListView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsYossi,)

    def get_queryset(self):
        
        post_title = self.request.query_params.get('title', None)
        if post_title is not None:
            queryset = Post.objects.filter(title=post_title)
        else:
            queryset = Post.objects.all()

        return queryset
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
  
class PostDetailView(RetrieveAPIView):
    permission_classes = (IsBen, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
class AuthorView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    









# ---------------------GenericAPIView + Mixins-------------------
class PostMixinListView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# ---------------------APIView------------------
# class PostView(APIView):

#     permission_classes = (AllowAny, )

#     def get(self, request, *args, **kwargs):

#         pk = kwargs.get('pk')
        
#         if pk:
#             try:
#                 instance = Post.objects.get(id=pk)
#                 serializer = PostSerializer(instance)
#             except Post.DoesNotExist:
#                 return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
#         else:
#             queryset = Post.objects.all()
#             serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)
    
    # def post(self, request, *args, **kwargs):

    #     serializer = PostSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, *args, **kwargs):

#         pk = kwargs.get('pk')
        
#         if pk:
#             try:
#                 post = Post.objects.get(id=pk)
#                 post.delete()
#                 return Response({"detail": "Post was deleted!"}, status=HTTP_202_ACCEPTED)
#             except Post.DoesNotExist:
#                 return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)

#         else:
#             return redirect('post-list')

    # def put(self, request, *args, **kwargs):

    #     pk = kwargs.get('pk')

    #     if pk:
    #         try:
    #             post = Post.objects.get(id=pk)
    #             serializer = PostSerializer(post, data=request.data)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return Response(serializer.data)
                
    #         except Post.DoesNotExist:
    #             return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
    #     else:
    #        return Response({"detail": "pk wasn't found"}, status=HTTP_400_BAD_REQUEST) 