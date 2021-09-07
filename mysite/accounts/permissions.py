from rest_framework.permissions import BasePermission

class IsSpecificType(BasePermission):
    check_user_type = None
    def has_permission(self, request, view):
        return request.user.user_type == self.check_user_type

class IsRider(IsSpecificType):
    message = 'You are not a rider!'
    check_user_type = 1

class IsDriver(IsSpecificType):
    message = 'You are not a driver!'
    check_user_type = 2