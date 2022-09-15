from rest_framework import permissions, generics
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, PostsListSerializer
from .models import UsersPost
from ..settings.classes import CreateRetrieveUpdateDestroy
from ..settings.permissions import IsUserAuthor, OwnerUserOnly


class PostView(CreateRetrieveUpdateDestroy):
    """
    CRUD for a user's post
    """
    queryset = UsersPost.objects.all().select_related('user')
    serializer_class = PostSerializer
    permission_classes_by_action = {'create': [OwnerUserOnly], 'retrieve': [permissions.AllowAny],
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
        return UsersPost.objects.filter(user_id=self.kwargs.get('pk'))