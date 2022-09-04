from rest_framework import generics, permissions, views, response
from src.usersprofile.models import UsersProfile
from .models import Follower
from .serializers import FollowersListSerializer


class FollowersListView(generics.ListAPIView):
    """
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = UsersProfile.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)