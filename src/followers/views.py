from rest_framework import generics, permissions, views, response
from src.usersprofile.models import UsersProfile
from .models import Follower
from .serializers import FollowersListSerializer, FolloweeListSerializer


class FollowersListView(generics.ListAPIView):
    """
    List of user's subscribers
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.kwargs['pk'])


class FolloweeListView(generics.ListAPIView):
    """
    List of user's followee
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolloweeListSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.kwargs['pk'])

class AddDeleteFollowerView(views.APIView):
    """
    Follow/unfollow a user
    """
    lookup_field = 'pk2'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, pk2):
        try:
            user = UsersProfile.objects.get(id=pk2)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        if not Follower.objects.filter(subscriber=request.user, user=user).exists() and request.user.id != pk2 and pk == request.user.id:
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        else:
            return response.Response(status=403)

    def delete(self, request, pk, pk2):
        try:
            sub = Follower.objects.get(subscriber=request.user, user=pk2)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        if pk == request.user.id:
            sub.delete()
            return response.Response(status=204)
        else:
            return response.Response(status=403)


class DeleteFolloweeView(views.APIView):
    """
    Delete a user's subscriber
    """
    lookup_field = 'pk2'
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, pk2):
        try:
            sub = Follower.objects.get(user=request.user, subscriber=pk2)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        if pk == request.user.id:
            sub.delete()
            return response.Response(status=204)
        else:
            return response.Response(status=403)