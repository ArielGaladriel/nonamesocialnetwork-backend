from rest_framework import permissions, generics

from .serializers import PostSerializer, PostsListSerializer
from .models import UsersPost
from ..settings.classes import CreateRetrieveUpdateDestroy
from ..settings.permissions import IsUserAuthor


class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD
    """
    queryset = UsersPost.objects.all().select_related('user')
    serializer_class = PostSerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated], 'retrieve': [permissions.AllowAny],
                                    'update': [IsUserAuthor],
                                    'destroy': [IsUserAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostsListView(generics.ListAPIView):
    '''
    '''
    queryset = UsersPost
    serializer_class = PostsListSerializer

    def get_queryset(self):
        return UsersPost.objects.filter(user_id=self.kwargs.get('pk'))