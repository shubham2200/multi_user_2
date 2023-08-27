from rest_framework.permissions import BasePermission

class IsVendorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_vendor
        # return False

    


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_user