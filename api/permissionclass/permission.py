from rest_framework.permissions import BasePermission

class IsR1User(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous and \
                super(IsR1User, self).has_permission(request, view):
            if request.user.usertype in ['R1']:
                return True
        return False

class IsR3orR1User(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous and \
                super(IsR3orR1User, self).has_permission(request, view):
            if request.user.usertype in ['R3','R1']:
                return True
        return False

class IsR2orR1User(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous and \
                super(IsR2orR1User, self).has_permission(request, view):
            if request.user.usertype in ['R2','R1']:
                return True
        return False