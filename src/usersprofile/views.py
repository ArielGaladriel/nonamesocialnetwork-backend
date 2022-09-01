from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import UsersProfile, UsersBio
from .serializers import ProfileSerializer, SettingsSerializer, BioSerializer


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


class BioSettingsView(ModelViewSet):
    """
    """
    serializer_class = BioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = UsersBio
        obj = get_object_or_404(queryset, user=self.kwargs.get("pk"))
        return obj
