from django.contrib import admin
from django.urls import path, include
from managment.views import (DepartmentListView, 
                             EmployeeListView, 
                             ProjectDetailView, 
                             ProjectUpdateView, 
                             ProjectDeleteView, 
                             TaskDetailView, 
                             TaskUpdateView,
                             TaskDeleteView,
                             ProjectMixinListView,
                             TaskMixinListView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('employee/', EmployeeListView.as_view(), name='employees-list'), 
    path('project/', ProjectMixinListView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project-delete'),
    path('task/', TaskMixinListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
]