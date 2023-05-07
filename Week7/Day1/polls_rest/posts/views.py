from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, 
                                        IsAuthenticated, 
                                        AllowAny)
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_202_ACCEPTED)

# Create your views here.

class PostView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')

        if pk:
            try:
                instance = Post.objects.get(id=pk)
                serializer = PostSerializer(instance)
            except Post.DoesNotExist:
                return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
        else: 
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')

        if pk:
            try:
                post = Post.objects.get(id=pk)
                post.delete()
                return Response({"detail": "Post was deleted!"}, status=HTTP_202_ACCEPTED)
            except Post.DoesNotExist:
                return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return redirect('post-list')
        

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if pk:
            try:
                post = Post.objects.get(id=pk)
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

            except Post.DoesNotExist:
                return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"detail": "pk wasn't found"}, status=HTTP_400_BAD_REQUEST)









# @csrf_exempt
# def post_view(request, article_pk):

#     try:
#         article = Post.objects.get(pk=article_pk)

#     except Post.DoesNotExist:
#         return HttpResponse(status=404) # Not found
    
#     if request.method == 'GET':
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return JsonResponse(data=serializer.data, safe=False)
    
#     if request.method == 'POST':
#         article_data = JSONParser.parse(request)
        
#         serializer = PostSerializer(data = article_data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201) #successfully
        
#         return JsonResponse(serializer.errors, status=400)

    
