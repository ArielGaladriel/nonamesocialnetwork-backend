from django.contrib.auth.views import LoginView
from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from djoser import signals
from djoser.compat import get_user_email
from djoser.conf import settings

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
    permission_classes = [IsUsersProfile]


class BioSettingsView(ModelViewSet):
    """
    """
    serializer_class = BioSerializer
    permission_classes = [IsUsersBio]

    def get_object(self):
        queryset = UsersBio
        obj = get_object_or_404(queryset, user=self.kwargs.get("pk"))
        self.check_object_permissions(self.request, obj)
        return obj


class CreateUserView(generics.CreateAPIView):
    """
    """
    queryset = UsersProfile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileCreationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
        context = {"user": user}
        to = [get_user_email(user)]
        settings.EMAIL.activation(self.request, context).send(to)


class MyLoginView(LoginView):
    """
    """

    def get_success_url(self):
        pk = self.request.user.id
        return reverse('my_account', args=[pk])