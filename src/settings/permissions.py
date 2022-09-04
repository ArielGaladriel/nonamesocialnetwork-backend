from rest_framework.permissions import BasePermission


class IsUsersProfile(BasePermission):
    """
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsUsersBio(BasePermission):
    """
    """

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id  # field "user" of UsersBio refers to an instance of UsersProfile


class IsUserAuthor(BasePermission):
    """
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

