from django.shortcuts import render
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

# Create your views here.

class PostView(APIView):

    permission_classes = (IsAdminUser)

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)










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

    
