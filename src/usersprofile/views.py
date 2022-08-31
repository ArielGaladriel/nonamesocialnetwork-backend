from rest_framework.viewsets import ModelViewSet

from .models import UsersBio, UsersProfile
from .serializers import BioSerializer, ProfileSerializer


class UsersProfileView(ModelViewSet):
    """
    """
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return UsersProfile.objects.filter(id=self.kwargs.get("pk"))