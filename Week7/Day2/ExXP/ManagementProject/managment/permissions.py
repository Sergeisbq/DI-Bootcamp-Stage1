from rest_framework import permissions
from .models import Employee


class IsDepartmentAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        print ("*****************", request.user.user_connect.administrator)
        if request.user.user_connect.administrator is True:
            return True
        return False
    

class IsDepartmentAdminObj(permissions.BasePermission):

    def has_obj_permission(self, request, view, obj):
        print ("*****************", request.user.user_connect.administrator)
        if request.user.user_connect.administrator is True:
            return True
        return False