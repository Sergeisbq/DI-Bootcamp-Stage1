from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
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


class StudentListView(APIView):

    # permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):

        date_joined_param = request.GET.get('date_joined')
        if date_joined_param:
            queryset = Student.objects.filter(date_joined=date_joined_param)
        else:
            queryset = Student.objects.all()
            
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    


class StudentDetailView(APIView):

    # permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')

        if pk:
            try:
                instance = Student.objects.get(id=pk)
                serializer = StudentSerializer(instance)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)
        else: 
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

    # def post(self, request, *args, **kwargs):

    #     serializer = PostSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=HTTP_200_OK)
        
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if pk:
            try:
                student_upd = Student.objects.get(id=pk)
                serializer = StudentSerializer(student_upd, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"detail": "pk wasn't found"}, status=HTTP_400_BAD_REQUEST)
        

    def delete(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')

        if pk:
            try:
                student_del = Student.objects.get(id=pk)
                student_del.delete()
                return Response({"detail": "Post was deleted!"}, status=HTTP_202_ACCEPTED)
            except Student.DoesNotExist:
                return Response({"detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return redirect('post-list')