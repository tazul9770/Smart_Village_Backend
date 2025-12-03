from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.user == request.user
        return True


        