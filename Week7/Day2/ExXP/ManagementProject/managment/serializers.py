from rest_framework import serializers
from .models import Department, Employee, Task, Project


class DepartmentSerializer(serializers.ModelSerializer):

    # author = serializers.HyperlinkedIdentityField(view_name='departments')

    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    project = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    tasks = serializers.HyperlinkedIdentityField(view_name='task-detail')

    class Meta:
        model = Project
        fields = '__all__'