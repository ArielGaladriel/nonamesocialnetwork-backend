from rest_framework import permissions, generics
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .serializers import PostSerializer, PostsListSerializer
from .models import UsersPost
from ..followers.models import Follower
from ..settings.classes import CreateRetrieveUpdateDestroy
from ..settings.permissions import IsUserAuthor, OwnerUserOnly, PostPrivacy


class PostView(CreateRetrieveUpdateDestroy):
    """
    CRUD for a user's post
    """
    queryset = UsersPost.objects.all().select_related('user')
    serializer_class = PostSerializer
    permission_classes_by_action = {'create': [OwnerUserOnly], 'retrieve': [PostPrivacy],
                                    'update': [IsUserAuthor],
                                    'destroy': [IsUserAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        if self.request.method == 'POST':
            filter_kwargs = {self.lookup_field: self.kwargs['pk']}
        else:
            filter_kwargs = {self.lookup_field: self.kwargs['pk3']}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class PostsListView(generics.ListAPIView):
    """
    View all user's posts
    """
    queryset = UsersPost
    serializer_class = PostsListSerializer

    def get_queryset(self):
        if self.kwargs.get('pk') == self.request.user.id:
            return UsersPost.objects.filter(user_id=self.kwargs.get('pk'))
        elif Follower.objects.filter(
                user=self.kwargs.get('pk'), subscriber=self.request.user.id, status='confirmed'):
            return UsersPost.objects.filter(Q(user_id=self.kwargs.get('pk')), (Q(privacy='public') |
                                                                               Q(privacy='followers only')))
        else:
            return UsersPost.objects.filter(user_id=self.kwargs.get('pk'), privacy='public')