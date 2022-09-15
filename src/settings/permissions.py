from rest_framework.permissions import BasePermission

from src.followers.models import Follower


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


class OwnerUserOnly(BasePermission):
    """
    Weird permission.
    Just to ensure that creation of a post is available from url were pk = user.id only
    UPD: also provides access for owner user only
    """

    def has_permission(self, request, view):
        return view.kwargs.get('pk') == request.user.id


class ProfilePrivacy(BasePermission):
    """
    Permission that depends on privacy settings of a user's profile
    """

    def has_object_permission(self, request, view, obj):
        if obj.privacy == 'public':
            return True
        elif obj.privacy == 'private' and obj.username == request.user:
            return True
        elif obj.privacy == 'followers only' and Follower.objects.filter(
                user=obj.id, subscriber=request.user.id, status='confirmed'):
            return True
        else:
            return False
