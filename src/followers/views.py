from rest_framework import generics, permissions, views, response
from src.usersprofile.models import UsersProfile
from .models import Follower
from .serializers import FollowersListSerializer, FolloweeListSerializer
from ..settings.permissions import OwnerUserOnly


class FollowersListView(generics.ListAPIView):
    """
    List of user's subscribers
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.kwargs['pk'], status='confirmed')


class FollowersRequestsListView(generics.ListAPIView):
    """
    List of users who wants to subscribe
    """
    permission_classes = [OwnerUserOnly]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.kwargs['pk'], status='requested')


class FolloweeListView(generics.ListAPIView):
    """
    List of user's followee
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolloweeListSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.kwargs['pk'], status='confirmed')


class FolloweeRequestsListView(generics.ListAPIView):
    """
    List of user's requested subscriptions
    """
    permission_classes = [OwnerUserOnly]
    serializer_class = FolloweeListSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.kwargs['pk'], status='requested')


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
            if user.privacy == 'public':
                Follower.objects.create(subscriber=request.user, user=user, status='confirmed')
            else:
                Follower.objects.create(subscriber=request.user, user=user, status='requested')
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


class UpdateDeleteFolloweeView(views.APIView):
    """
    Delete a user's subscriber
    """
    lookup_field = 'pk2'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, pk2):
        try:
            sub = Follower.objects.get(user=request.user, subscriber=pk2, status='requested')
        except Follower.DoesNotExist:
            return response.Response(status=404)
        if pk == request.user.id:
            sub.status = 'confirmed'
            sub.save()
            return response.Response(status=204)
        else:
            return response.Response(status=403)

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