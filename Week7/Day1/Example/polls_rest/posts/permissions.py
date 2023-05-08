from rest_framework import permissions


class IsYossi(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.username == 'yossi':
            return False
        return True
    

class IsBen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.title == 'Test5' and request.user.username == 'sergeiboiko':
            return False
        return True



