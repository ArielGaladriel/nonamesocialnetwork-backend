from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import UsersProfile, UsersBio
from .serializers import ProfileSerializer, SettingsSerializer, BioSerializer, ProfileCreationSerializer

from ..settings.permissions import IsUsersProfile, IsUsersBio


class UsersProfileView(ModelViewSet):
    """
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return UsersProfile.objects.filter(id=self.kwargs.get("pk"))


class UserSettingsView(ModelViewSet):
    """
    """
    queryset = UsersProfile
    serializer_class = SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {'get': [IsUsersProfile], 'update': [IsUsersProfile]}


class BioSettingsView(ModelViewSet):
    """
    """
    serializer_class = BioSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {'get': [IsUsersBio], 'update': [IsUsersBio]}

    def get_object(self):
        queryset = UsersBio
        obj = get_object_or_404(queryset, user=self.kwargs.get("pk"))
        return obj


class CreateUserView(generics.CreateAPIView):
    queryset = UsersProfile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileCreationSerializer
