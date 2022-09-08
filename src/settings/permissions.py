from rest_framework.permissions import BasePermission


class IsUsersProfile(BasePermission):
    """
    Owner (for a user's information from UsersProfile model) - current authorized user
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsUsersBio(BasePermission):
    """
    Owner (for a user's information from UsersBio model) - current authorized user
    """

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id  # field "user" of UsersBio refers to an instance of UsersProfile


class IsUserAuthor(BasePermission):
    """
    Author of the post - current authorized user
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and view.kwargs.get('pk') == request.user.id


class IsUserCreator(BasePermission):
    """
    Weird permission. Will be deleted.
    Just to ensure that creation of a post is available from url were pk = user.id only
    """

    def has_permission(self, request, view):
        return view.kwargs.get('pk') == request.user.id
