from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Department, Employee, Task, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, TaskSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)

from .permissions import IsDepartmentAdmin

from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED,
                                   HTTP_400_BAD_REQUEST)

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import mixins

# Create your views here.


class DepartmentListView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = (IsDepartmentAdmin, )

    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProjectMixinListView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class TaskMixinListView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsDepartmentAdmin, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class EmployeeListView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsDepartmentAdmin, )

    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class ProjectDetailView(RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDeleteView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskDetailView(RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer