from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        proper_perm = bool(request.user and request.user.is_staff)
        if request.method =="GET" and proper_perm :
            return True
        else: 
            return False
        
class ReviewUserReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       else:
           return request.user == obj.review_user
       
        